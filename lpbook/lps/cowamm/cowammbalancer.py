

import asyncio
from copy import deepcopy
from dataclasses import dataclass
from async_lru import alru_cache
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

from lpbook import LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy, LPSyncProxy, MultiLPFromInitialStatePlusChangesProxy
from lpbook.lps.balancer_v2 import BalancerV2Weighted
from lpbook.util import LP, traced
from lpbook.web3 import BlockId, TokenDB
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream
from web3.exceptions import BlockNotFound, ContractLogicError
from .common import COWAMM, COWSwapWeb3Proxy
from lpbook.error import TemporaryError

logger = logging.getLogger(__name__)

 
@dataclass
class COWAMMBalancer(COWAMM):
    """Balancer Cow AMM."""
    app_data: str

    @property
    def execution_info(self) -> Dict:
        return {
            "encoding_parameters": {
                "app_data": self.app_data
            }
        }
    
    @property
    def gas_stats(self) -> Dict:
        return {
            'mean': 120000, 
            'stddev': 0, 
        }

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'COWAMMBalancer'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '1'

    
class BPoolContractProxy:
    def __init__(self, lp_id, web3_client):
        self.web3_client = web3_client
        with open(Path(__file__).parent / 'artifacts' / 'BCowPool.abi', 'r') as f:
            contract_abi = f.read()
            lp_id_chksum = web3_client.to_checksum_address(lp_id)
            self.contract = web3_client.eth.contract(
                address=lp_id_chksum,
                abi=contract_abi
            )

    @alru_cache
    async def get_tokens(self):
        return await self.contract.functions.getFinalTokens().call()

    async def get_balance_no_cache(self, token_address, block_identifier="latest"):
        return await self.contract.functions.getBalance(self.web3_client.to_checksum_address(token_address)).call(block_identifier=block_identifier)

    @alru_cache
    async def get_balance_cached(self, token_address, block_identifier="latest"):
        return await self.get_balance_no_cache(token_address, block_identifier=block_identifier)

    async def get_balance(self, token_address, block_identifier="latest"):
        if block_identifier == "latest":
            return await self.get_balance_no_cache(token_address, block_identifier=block_identifier)
        else:
            return await self.get_balance_cached(token_address, block_identifier=block_identifier)

    async def get_weight_no_cache(self, token_address, block_identifier="latest"):
        return await self.contract.functions.getNormalizedWeight(self.web3_client.to_checksum_address(token_address)).call(block_identifier=block_identifier)  

    @alru_cache
    async def get_weight_cached(self, token_address, block_identifier="latest"):
        return await self.get_weight_no_cache(token_address, block_identifier=block_identifier)

    async def get_weight(self, token_address, block_identifier="latest"):
        if block_identifier == "latest":
            return await self.get_weight_no_cache(token_address, block_identifier=block_identifier)
        else:
            return await self.get_weight_cached(token_address, block_identifier=block_identifier)

    async def get_app_data_no_cache(self, block_identifier="latest"):
        return await self.contract.functions.APP_DATA().call(block_identifier=block_identifier)

    @alru_cache
    async def get_app_data_cached(self, block_identifier="latest"):
        return await self.get_app_data_no_cache(block_identifier=block_identifier)
    
    async def get_app_data(self, block_identifier="latest"):
        if block_identifier == "latest":
            return await self.get_app_data_no_cache(block_identifier=block_identifier)
        else:
            return await self.get_app_data_cached(block_identifier=block_identifier)


class COWAMMBalancerAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the cow amm balancer LP through web3."""

    def __init__(self, lp_ids, web3_client, token_db: TokenDB):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.web3_client = web3_client
        self.token_db = token_db
        self.contracts = {lp_id: BPoolContractProxy(lp_id, web3_client) for lp_id in lp_ids}
        self.weights = {lp_id: None for lp_id in lp_ids}
        self.app_data = {lp_id: None for lp_id in lp_ids}
 
    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block("latest")
        return BlockId.from_web3(block)

    async def get_lp_tokens(self, lp_id):
        return await self.contracts[lp_id].get_tokens()
    
    async def get_tokens(self, lp_id) -> list[Tuple]:
        token_ids = await self.get_lp_tokens(lp_id)
        tokens = [
            await self.token_db.get(t.lower()) 
            for t in token_ids
        ]
        return tokens

    async def read_lp_data(self, lp_id, tokens, block_identifier):
        balances = [
            await self.contracts[lp_id].get_balance(t.address, block_identifier=block_identifier)            
            for t in tokens
        ]
        # Assume app data will not change to speed up things
        if self.weights[lp_id] is None:
            self.weights[lp_id] = [
                await self.contracts[lp_id].get_weight(t.address, block_identifier=block_identifier)            
                for t in tokens
            ]
        # Assume app data will not change to speed up things
        if self.app_data[lp_id] is None:
            app_data_as_byte_array = await self.contracts[lp_id].get_app_data(block_identifier=block_identifier)
            self.app_data[lp_id] = "0x" + app_data_as_byte_array.hex()
        return balances, self.weights[lp_id], self.app_data[lp_id]

    async def create_from_blockchain(self, lp_id, block: BlockId) -> COWAMMBalancer:
        block_identifier = block.to_web3()

        tokens = await self.get_tokens(lp_id)
        balances, weights, app_data = await self.read_lp_data(lp_id, tokens, block_identifier)
        total_weight = sum(weights)
        weights = [w/total_weight for w in weights ]

        lp = BalancerV2Weighted(_id=lp_id, all_tokens=tokens, balances=balances, weights=weights, fee_e18=0, type="Weighted", owner="0x")
        return COWAMMBalancer(
            lp=lp,
            app_data=app_data
        )

    @traced(logger, "Retrieving cow amm balancer v2 state from blockchain")
    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        state = {}

        async def add_to_state(lp_id):
            try:
                state[lp_id] = await self.create_from_blockchain(lp_id, block)
            except BlockNotFound as e:
                raise TemporaryError(str(e))
            except ContractLogicError as e:
                logger.error(
                    f"Transaction reverted when querying pool {lp_id}. Consider denylisting."
                )
                raise e
            except ValueError as e:
                if e.args[0]['code'] == -32000:
                    raise TemporaryError(str(e))
                raise e

        await asyncio.gather(
            *[add_to_state(lp_id) for lp_id in self.lp_ids]
        )

        #logger.debug(state)
        return state



class COWAMMBalancerWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries async proxy for an initial state, and web3 for state updates."""

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / 'BCowPool.abi', 'r') as f:
            contract_abi = f.read()
        BCowPool = web3_client.eth.contract(abi=contract_abi)

        super().__init__(
            lp_ids,
            [BCowPool.events.LOG_EXIT, BCowPool.events.LOG_JOIN],
            async_proxy,
            event_stream,
            web3_client
        )

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""

        lp_id = d.address.lower()
        assert lp_id in state.keys()
        lp = state[lp_id]

        if d.event == 'LOG_EXIT':
            token_out_address = d.args.tokenOut.lower()
            token_out_index = [t.address == token_out_address for t in lp.tokens].index(True)
            lp.lp.balances[token_out_index] -= d.args.tokenAmountOut

        elif d.event == 'LOG_JOIN':
            token_in_address = d.args.tokenIn.lower()
            token_in_index = [t.address == token_in_address for t in lp.tokens].index(True)
            lp.lp.balances[token_in_index] += d.args.tokenAmountIn

        else:
            assert False


class COWAMMBalancerDriver(LPDriver):
    def __init__(
        self,
        event_stream: EventStream,
        block_stream: BlockStream,
        token_db: TokenDB,
        web3_client=None
    ):
        super().__init__(COWAMMBalancer)
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.token_db = token_db
        self.web3_client = web3_client
        self.initialized = False
 
    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        if data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.Web3
        ]:
            async_proxy = COWAMMBalancerAsyncProxy(
                lp_ids, self.web3_client, self.token_db
            )
            #return LPSyncProxyFromAsyncProxy(async_proxy, self.block_stream)
            cow_swap_proxy = COWSwapWeb3Proxy(lp_ids, async_proxy, self.event_stream, self.web3_client)
            cow_amm_balancer_proxy = COWAMMBalancerWeb3Proxy(lp_ids, async_proxy, self.event_stream, self.web3_client)
            proxy = MultiLPFromInitialStatePlusChangesProxy([cow_swap_proxy, cow_amm_balancer_proxy])
            return proxy
        else:
            assert False # No other proxies are currently implemented for balancer.

    async def has_significant_liquidity(self, lp_id, bpool, tokens):
        weth_address = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
        wsteth_address = "0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0"
        weeth_address = "0xcd5fe23c85820f7b72d0926fc9b05b43e359b7ee"
        sfrxeth = "0xac3e018457b222d93114458476f3e3416abbe38f"
        usdc_address = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
        usdt_address = "0xdac17f958d2ee523a2206206994597c13d831ec7"
        sdai_address = "0x83f20f44975d03b1b09e64809b757c47f942beea"
        for ethlike_adress in [weth_address, wsteth_address, weeth_address,sfrxeth]:
            if ethlike_adress in tokens:
                return await bpool.get_balance(ethlike_adress) >= 0.5e18
        for usdlike_address in [usdc_address, usdt_address, sdai_address]:
            if usdlike_address in tokens:
                return await bpool.get_balance(usdlike_address) >= 1000

        logger.debug(f"Don't know if cowammbalancer amm {lp_id} has significant liquidity. Including just in case.")
        return True # Being conservative for other tokens

    async def has_bad_tokens(self, bpool, tokens):
        bad_tokens = {
            "0xedb171c18ce90b633db442f2a6f72874093b49ef",
            "0x2e135a0c0d43dde20193416139dbdc2f5e8f2359",
            "0xf25a3b5a965c59f88873da93fc2a244b00616be4",
            "0x7f4b66ff703336cfc35b901144614496ae0b0d27",
            "0xd9fcd98c322942075a5c3860693e9f4f03aae07b"
        }
        return len(bad_tokens & set(tokens)) > 0
    
    async def should_include_lp(self, lp_id):
        blacklisted_ids = {
            #"0x9b8b93fc2a454f4f0f240aaf6644dbd77a528246",
            #"0x477a8982515e3a3d3aa6447b019b7c647e4162f8"
        }
        bpool = BPoolContractProxy(lp_id, self.web3_client)
        tokens = {t.lower() for t in await bpool.get_tokens()}
        return lp_id not in blacklisted_ids and await self.has_significant_liquidity(lp_id, bpool, tokens) and not await self.has_bad_tokens(bpool, tokens)
    
    async def get_lp_ids_from_blockchain(self):
        lp_ids = [
            '0xf08d4dea369c456d26a3168ff0024b904f2d8b91',  # USDC-WETH 
            '0x6ff0531ee19272675b3c7d30401a5b2b2c7b0c67',  # COW-WETH
            '0x9fb7106c879fa48347796171982125a268ff0630',  # MKR-WETH
            '0xf8f5b88328dff3d19e5f4f11a9700293ac8f638f',  # BAL-WETH 
            '0x4359a8ea4c353d93245c0b6b8608a28bb48a05e2',  # ARB-WETH
            '0xf706c50513446d709f08d3e5126cd74fb6bfda19',  # AAVE-WETH
            '0xdfee48c9df6d26c734296c0e6bd02401100a7217',  # DOG-WSTETH
            '0x9bd702e05b9c97e4a4a3e47df1e0fe7a0c26d2f1',  # COW-WSTETH 
            '0xfec04c31b6099ce76c4c5d6d754a34141884fd91',  # GNO-WSTETH
            '0x41ff63c864097a7fbdf206fe676223e29f729fcb',  # GHO-WETH
            '0xcc8b8d38b34c1888c15176ffec12593d78908351',  # PEPE-WETH
            '0x9d0e8cdf137976e03ef92ede4c30648d05e25285',  # DOG-WSTETH
            '0xcf9fe5e9bd841aec785d1df3371b7c60daeb8467',  # RPL-WETH
            '0xd7855be714943928236bda82d9cd7caf189f2806',  # USDT-USDC
            '0x7c838b3ed3c15a5d5032e809b8714f0ae5e9a821',  # WETH-wNXM 
            '0x3b124c8b4846836ba52df6cb6576ef66ca167dc1',   # WETH-FOX
            '0xbf8868b754a77e90ea68ffc0b5b10a7c729457e1', 
            '0x42d9e44eed903a0ee477c9c04d1d1730c5e87272', 
            '0xb3d37552eebbbdbea36258ba0948f4bbcaa3584e', 
            '0x11f2a400de0a2fc93a32f88d8779d8199152c6a4', 
            '0xa7401066570960894a12b403f461cb61e8804b7b', 
            '0x96f8dfa1e922f88c313052d5357cc6a910e19c1e', 
            '0xa62e2c047b65aee3c3ba7fc7c2bd95c82a514de2', 
            '0x1e45ea24cd5128c52c1e207154c61849f0cc1035', 
            '0x8ec257dc0b17b0c862d428c801fdcc8c382bf918', 
            '0x0c8ee93df5a4bad1c6f05e2676f87e6440b0b956', 
            '0x75eb3d7976f0bf848f4bc22a7563fa50bd73c504', 
            '0xf25a3b5a965c59f88873da93fc2a244b00616be4', 
            '0x28874461760a94b7b4fa4cd8f8f1734a7b3684fd', 
            '0x06966b4ae338ce20f283086914388133f27d1d3e', 
            '0xf544694542ca8ffcd1120ff11ffa33bca475bce6', 
            '0x54f26633b95ce09b1da0d02194ca84c45ab14ac8', 
            '0x06eda3e560f8589d388785d92dd1c56831d01546', 
            '0x43653ae64ea32987dbe270ea992536c3eed82df7', 
            '0x547bfddb2ab8d83f24a9747980a7e00c221e0220', 
            '0xeda4581b03442ea84307844c2337e008cb057454', 
            '0x0ce69a796abe0c0451585aa88f6f45ebac9e12dc', 
            '0xa81b22966f1841e383e69393175e2cc65f0a8854',
            '0x503cf7250888f4422d0bfbe5c30e7a6b4716fecf', 
            '0x891a539d008f69e62f22902877cce54a58644cae', 
            '0x9a2a304a036d9da289656e95b58c72692b515e95', 
            '0x9dff17c7b47c4cea638e37fd94ee85798ccbc6c2', 
            '0x7e31ae101acaad809e377a9f88dbc4c486ab0191', 
            '0xc368c0106f5a41c262e476494623cadae4e11f80', 
            '0x40c1551d93e51f3278d2471465fe4017f54e290a', 
            '0x03a0cc954c800920ceb6f4c67f6b1ef5df42dcca', 
            '0x777a11c830ce8a7c3d325b0be020f7ba7edf2b58', 
            '0x3544e78c40b209a94f2ce7b89078b2d147f4b1c8',
            '0x269e42f06c7977e91644bb30bff627d483b6e73c',
            '0x7529d8ac08d4dddc159bc8809a971a7605c34f80',
            '0xebb8eec34ff7f10771c929e572b2906f2f405439'
            ]

        try:
            FACTORY_CONTRACT_ADDRESS = "0xf76c421bAb7df8548604E60deCCcE50477C10462"
            #FACTORY_CONTRACT_DEPLOYMENT_BLOCK = 20432455
            FROM_BLOCK = 22150571 + 1
            with open(Path(__file__).parent / 'artifacts' / 'BCowFactory.abi', 'r') as f:
                contract_abi = f.read()
                BCowFactory = self.web3_client.eth.contract(
                    address=FACTORY_CONTRACT_ADDRESS,
                    abi=contract_abi
                )
            logs = await BCowFactory.events.COWAMMPoolCreated().get_logs(from_block=FROM_BLOCK)
            new_lp_ids = [log_entry.args.bCoWPool.lower() for log_entry in logs]
            lp_ids += new_lp_ids
        except:
            logger.exception("Error while querying cowammbalancerv2 updated list of pool.")
            pass
        lp_ids = [lp_id for lp_id in lp_ids if await self.should_include_lp(lp_id)]
        return lp_ids

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        if self.initialized:
            return self.lp_ids
        lp_ids = await self.get_lp_ids_from_blockchain()
        lp_ids = list(
            set(lp_ids) - 
            {
                "0x9fb7106c879fa48347796171982125a268ff0630"  # MKR token is odd
            }
        )
        self.initialized = True
        return lp_ids

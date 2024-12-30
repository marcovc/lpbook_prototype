

import asyncio
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
import logging
from pathlib import Path
from typing import Any, Dict, List

from lpbook import LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy, LPSyncProxy
from lpbook.lps.balancer_v2 import BalancerV2Weighted
from lpbook.lps.cowamm.common import COWAMM
from lpbook.util import LP, Token, traced
from lpbook.web3 import BlockId, TokenDB, get_erc20_contract
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream
from web3.exceptions import BlockNotFound, ContractLogicError
from lpbook.error import TemporaryError
from eth_account.messages import encode_defunct
from eth_account import Account

logger = logging.getLogger(__name__)
    
@dataclass
class COWAMMPrivate(COWAMM):
    """Private Cow AMM."""
    address: str
    state_hash: str    
    reserves_address: str

    @property
    def execution_info(self) -> Dict:
        return {
            "encoding_parameters": {
                "address": self.address,
                "state_hash": self.state_hash,
                "reserves_address": self.reserves_address
            }
        }
    
    @property
    def gas_stats(self) -> Dict:
        return {
            'mean': 50000, 
            'stddev': 0, 
        }

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'COWAMMPrivate'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '1'


#def create_signature(proxy_address, nonce, proxy_address_private_key, web3):
#    proxy_address = web3.to_checksum_address(proxy_address)
#    message_hash = web3.solidity_keccak(["address", "uint256"],[proxy_address, nonce])
#    eth_signed_message = encode_defunct(primitive=message_hash)
#    signature = Account.sign_message(eth_signed_message, private_key=proxy_address_private_key)
#    return signature.signature.hex()

def updated_state_hash(prev_state_hash: str, amounts_in: List[int], amounts_out: List[int], web3_client):
    return web3_client.solidity_keccak(
        ["bytes32", "uint256[]", "uint256[]"],
        [prev_state_hash, amounts_in, amounts_out]
    ).to_0x_hex()
    
class COWAMMPrivateAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the cow amm private LP through web3."""

    def __init__(
            self, 
            lp_ids: list[str], 
            lp_tokens: dict[str, List[Token]], 
            lp_weights: dict[str, List[float]], 
            lp_fees: dict[str, float],
            web3_client
        ):
        self.lp_ids = lp_ids
        self.lp_tokens = lp_tokens
        self.lp_weights = lp_weights
        self.lp_fees = lp_fees
        self.web3_client = web3_client
        all_tokens = [token for tokens in lp_tokens.values() for token in tokens]
        self.token_contracts = {token.address : get_erc20_contract(token.address, web3_client) for token in all_tokens}
        with open(Path(__file__).parent / 'artifacts' / 'COWAMMPrivate.abi', 'r') as f:
            contract_abi = f.read()
        self.lp_contracts = {lp_id : web3_client.eth.contract(abi=contract_abi, address=web3_client.to_checksum_address(lp_id)) for lp_id in lp_ids}

    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block("latest")
        return BlockId.from_web3(block)
    
    async def get_balances(self, lp_id, reserves_address, block_identifier):
        address = self.web3_client.to_checksum_address(reserves_address)
        return await asyncio.gather(
            *[self.token_contracts[token.address].functions.balanceOf(address).call(block_identifier=block_identifier)            
            for token in self.lp_tokens[lp_id]]
        )

    async def get_state_hash(self, lp_id, block_identifier):
        return "0x"+ (await self.lp_contracts[lp_id].functions.stateHash().call(block_identifier=block_identifier)).hex()
        
    async def get_reserves_address(self, lp_id, block_identifier):
        # Accessing a private field.
        raw_data = await self.web3_client.eth.get_storage_at(self.lp_contracts[lp_id].address, 3, block_identifier=block_identifier)
        return self.web3_client.to_checksum_address(raw_data[-20:]).lower()
    
    async def create_from_blockchain(self, lp_id, block: BlockId) -> COWAMMPrivate:
        reserves_address = await self.get_reserves_address(lp_id, block.to_web3())
        balances, state_hash = await asyncio.gather(
            self.get_balances(lp_id, reserves_address, block.to_web3()),
            self.get_state_hash(lp_id, block.to_web3())
        )

        lp = BalancerV2Weighted(
            _id=lp_id, 
            all_tokens=self.lp_tokens[lp_id], 
            balances=balances,
            weights=self.lp_weights[lp_id], 
            fee_e18=self.lp_fees[lp_id] * int(1e18), 
            type="Weighted",
            owner="0x"
        )

        return COWAMMPrivate(
            lp=lp,
            address=lp_id,
            state_hash=state_hash,
            reserves_address=reserves_address
        )

    @traced(logger, "Retrieving cow amm private state from blockchain")
    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        state = {}

        async def create(lp_id):
            try:
                state[lp_id] = await self.create_from_blockchain(lp_id, block)
            except BlockNotFound as e:
                raise TemporaryError(str(e))
            except ContractLogicError as e:
                logger.error(
                    f"Transaction reverted when querying cowamm private pool {lp_id}."
                )
                raise e
            except ValueError as e:
                if e.args[0]['code'] == -32000:
                    raise TemporaryError(str(e))
                raise e

        await asyncio.gather(*[create(lp_id) for lp_id in self.lp_ids])

        #logger.debug(state)
        return state

class COWAMMPrivateSyncProxy(LPFromInitialStatePlusChangesProxy):
    """Queries Web3 for an initial state and for state updates."""

    def __init__(self, lp_ids: List[str], async_proxy, web3_client, event_stream):
        self.lp_ids = lp_ids
        self.web3_client = web3_client
        with open(Path(__file__).parent / 'artifacts' / 'COWAMMPrivate.abi', 'r') as f:
            contract_abi = f.read()
        COWAMMPrivate = web3_client.eth.contract(abi=contract_abi)
        super().__init__(
            lp_ids,
            [COWAMMPrivate.events.Rebalance],
            async_proxy,
            event_stream,
            web3_client
        )

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""
        address = d["address"].lower()
        assert address in self.lp_ids

        assert d.event == "Rebalance"

        lp = state[address]

        tokens_in = d.args.tokensIn
        amounts_in = d.args.amountsIn

        tokens_out = d.args.tokensOut
        amounts_out = d.args.amountsOut

        for token, amount in zip(tokens_in, amounts_in):
            token_index = [t.address == token.lower() for t in lp.tokens].index(True)                
            lp.lp.balances[token_index] += amount

        for token, amount in zip(tokens_out, amounts_out):
            token_index = [t.address == token.lower() for t in lp.tokens].index(True)                
            lp.lp.balances[token_index] -= amount

        lp.state_hash = updated_state_hash(lp.state_hash, amounts_in, amounts_out, self.web3_client)



# Check https://dune.com/banana1/cow-swap-main for a list of most traded tokens

TOKENS = {
    "WETH": {
        "address": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        "exposure": 1
    },
    "WBTC": {
        "address": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
        "exposure": 1
    },
    "USDC": {
        "address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        "exposure": 1
    },
    "COW": {
        "address": "0xdef1ca1fb7fbcdc777520aa7f396b4e015f497ab",
        "exposure": 1
    },
    "USDT": {
        "address": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "exposure": 1
    },
    # wstETH (wrapped LIDO stETH, that does not rebase)
    "wstETH": {
        "address": "0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0", 
        "exposure": 1
    },
     # ezETH (Enzo restaking ETH, also not rebasing)
    "ezETH": {
        "address": "0xbf5495efe5db9ce00f80364c8b423567e58d2110",
        "exposure": 0.5
    },
    # weETH  (wrapped ether.fi ETH, also not rebasing)
    "weETH": {
        "address": "0xcd5fe23c85820f7b72d0926fc9b05b43e359b7ee",
        "exposure": 0.2
    }
}

# Note on number and size of pools:
# Since the total volume pooled is divided by the number of assets, this means:
# * If there are many assets compared to the volume, the pool will be used for smaller trades
# but more often. 
# * If there are few assets compared to the volume, the pool will be used for larger trades
# but less often.
COWAMMPRIVATE_INSTANCES = {
    #"weth like pool" : ["WETH", "wstETH", "ezETH", "weETH"],
    #"other possibility" : ["WETH", "WBTC", "USDC", "USDT"],
    "0xb1ad40d67027596cbd8b9f5de90a2bb5811c82bc": {     # This is the proxy contract address, the portfolio address is obtained from the contract
        "tokens": ["WETH", "COW", "USDC"]
    },
}

class COWAMMPrivateDriver(LPDriver):
    def __init__(
        self,
        event_stream: EventStream,
        token_db: TokenDB,
        web3_client
    ):
        super().__init__(COWAMMPrivate)
        self.event_stream = event_stream
        self.token_db = token_db
        self.web3_client = web3_client

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:

        lp_tokens = {}
        lp_weights = {}
        lp_fees = {lp_id: 0 for lp_id in lp_ids}    # I think adding fee just mean it will rebalance less often, because the cowamm gets surplus anyway

        for lp_id in lp_ids:
            token_symbols = COWAMMPRIVATE_INSTANCES[lp_id]["tokens"]
            token_addresses = [TOKENS[symbol]["address"] for symbol in token_symbols]
            tokens = [await self.token_db.get(token) for token in token_addresses]
            weights = [TOKENS[symbol]["exposure"] for symbol in token_symbols]
            sum_weights = sum(weights)
            weights = [weight / sum_weights for weight in weights]
            lp_tokens[lp_id] = tokens
            lp_weights[lp_id] = weights

        if data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.Web3
        ]:
            async_proxy = COWAMMPrivateAsyncProxy(
                lp_ids, lp_tokens, lp_weights, lp_fees, self.web3_client
            )
            sync_proxy = COWAMMPrivateSyncProxy(
                lp_ids, async_proxy, self.web3_client, self.event_stream
            )
            return sync_proxy
        else:
            assert False # No other proxies are currently implemented for balancer.

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        return list(COWAMMPRIVATE_INSTANCES.keys())

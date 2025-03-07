

import asyncio
from copy import deepcopy
import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

from async_lru import alru_cache
from lpbook import LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy, LPSyncProxy
from lpbook.error import TemporaryError
from lpbook.lps.fixedrate.FixedRate import FixedRate
from lpbook.util import LP, Token, Trade
from lpbook.web3 import BlockId, create_token_from_web3
from web3.exceptions import BlockNotFound, ContractLogicError

from lpbook.web3.event_stream import EventStream

logger = logging.getLogger(__name__)

address_sUSDS = "0xa3931d71877c0e7a3148cb7eb4463524fec27fbd"
address_USDS = "0xdc035d45d973e3ec169d2276ddab16f1e407384f"

address_proxy_contract = address_sUSDS
address_implementation_contract = "0x4e7991e5c547ce825bdeb665ee14a3274f9f61e0"

def balances_from_drip(chi: int) -> Tuple[int, int]:
    # USDS -> sUSDS (deposit)
    # sUSDS = USDS * 10^27 / chi

    # sUSDS -> USDS (redeem)
    # USDS = sUSDS * chi / 10^27

    # Therefore the exchange rate is:
    # balance(sUSDS) / balance(USDS) = 10^27 / chi

    
    balance_usds = 100**6*10**18  # A large number similar to other fixed rate LPs.
    balance_susds = int(balance_usds * 10**27 / chi)

    return [balance_usds, balance_susds]    


class SUSDSAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the uniswap v2 LP through web3."""

    def __init__(self, web3_client):

        self.lp_id = address_proxy_contract
        self.web3_client = web3_client

        with open(Path(__file__).parent / 'artifacts' / 'susds.abi', 'r') as f:
            contract_abi = f.read()
        self.SUDSD = web3_client.eth.contract(abi=contract_abi, address=self.web3_client.to_checksum_address(self.lp_id))

    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block("latest")
        return BlockId.from_web3(block)

    @alru_cache
    async def get_tokens(self) -> Tuple[Token, Token]:
        token0_address = address_USDS   # USDS
        token1_address = address_sUSDS   # SUSDS

        token0_address = self.web3_client.to_checksum_address(token0_address)
        token1_address = self.web3_client.to_checksum_address(token1_address)

        return await asyncio.gather(
            create_token_from_web3(token0_address, self.web3_client),
            create_token_from_web3(token1_address, self.web3_client)
        )
        

    async def create_from_blockchain(self, block: BlockId) -> FixedRate:
        block_identifier = block.to_web3()

        token1, token2 = await self.get_tokens()
        drip = await self.SUDSD.functions.drip().call(block_identifier=block_identifier)
        max_sell_amount1, max_sell_amount2 = balances_from_drip(drip)

        return FixedRate(
            address=self.lp_id,
            token1=token1,
            token2=token2,
            max_sell_amount1=max_sell_amount1,
            max_sell_amount2=max_sell_amount2,
            gas=145000  # FIXME : made up value
        )

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        logger.debug(
            f'Retrieving sUSDS state from blockchain at block {block} ...'
        )

        state = {}

        try:
            state[self.lp_id] = await self.create_from_blockchain(
                block
            )
        except BlockNotFound as e:
            raise TemporaryError(str(e))
        except ContractLogicError as e:
            logger.error(
                f"Transaction reverted when querying SUDS contract."
            )
            raise e
        except ValueError as e:
            if e.args[0]['code'] == -32000:
                raise TemporaryError(str(e))
            raise e

        # logger.debug(state)
        return state


class SUSDSSyncProxy(LPFromInitialStatePlusChangesProxy):

    def __init__(self, async_proxy, event_stream, web3_client):
        with open(Path(__file__).parent / 'artifacts' / 'susds.abi', 'r') as f:
            contract_abi = f.read()
        SUDSD = web3_client.eth.contract(abi=contract_abi)

        super().__init__(
            [address_proxy_contract],
            [SUDSD.events.Drip],
            async_proxy,
            event_stream,
            web3_client
        )

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""
        lp = state[d.address.lower()]
        assert d.event == 'Drip'
        chi = d.args.chi
        lp.balances = balances_from_drip(chi)

    def get_trades(self, prev_state: Dict[str, LP], changes: List[Any]) -> list[Trade]:
        """Assembles list of trades from updates."""
        return []
    


class SUDSDDriver(LPDriver):
    def __init__(
        self,
        event_stream: EventStream,
        web3_client
    ):
        super().__init__(FixedRate)
        self.event_stream = event_stream
        self.web3_client = web3_client

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        async_proxy = SUSDSAsyncProxy(self.web3_client)
        assert list(lp_ids) == [async_proxy.lp_id]
        sync_proxy = SUSDSSyncProxy(
                async_proxy,
                self.event_stream,
                self.web3_client
            )
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        if address_sUSDS in token_ids:
            return [address_proxy_contract]
        return []
    
    @property
    def uid(self) -> str:
        return f"{self.protocol}-{self.kind}-susds"

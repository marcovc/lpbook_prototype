

import asyncio
from dataclasses import dataclass
import logging
from math import log, sqrt
from pathlib import Path
from typing import Dict, List, Optional, Set
import aiohttp

from lpbook import EventFilteredLPSyncProxyFromAsyncProxy, LPAsyncProxy, LPDriver, LPSyncProxy, LPSyncProxyFromAsyncProxy
from lpbook.error import TemporaryError
from lpbook.util import LP, Token, traced
from lpbook.web3 import BlockId, TokenDB
from lpbook.web3.block_stream import BlockStream
from web3.exceptions import BlockNotFound, ContractLogicError

from lpbook.web3.event_stream import EventStream

from .common import UniV3Like

logger = logging.getLogger(__name__)

@dataclass
class MaverickV2(UniV3Like):
    """Maverick V2 LP."""

    tick_limit_lb: int
    tick_limit_ub: int

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Maverick'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'

    @property
    def execution_info(self) -> Dict:
        execution_info = super().execution_info
        execution_info.update({
            'tick_limit_lb': self.tick_limit_lb,
            'tick_limit_ub': self.tick_limit_ub
        })
        return execution_info

    @property
    def gas_stats(self) -> Dict:
        # Guessed ...
        return {
            'mean': 110000
        }
    
class MaverickV2PoolDB:
    MIN_LIQUIDITY_USD = 3000

    def __init__(self, session: aiohttp.ClientSession, token_db: TokenDB):
        self.session = session
        self.token_db = token_db
        self.pools = {}
        self.initialized_event = asyncio.Event()

    async def run(self):
        self.running = True
        while self.running:
            try:
                await self.refresh()
                if not self.initialized_event.is_set():
                    self.initialized_event.set()
            except Exception as e:
                logger.error(f"Failed to refresh maverick pool DB: {e}. Retrying in 5 minutes.")
                self.session = aiohttp.ClientSession()
            await asyncio.sleep(5*60)
    
    async def query(self):
        async with self.session.get('https://v2-api.mav.xyz/api/latest/tickers?chainId=1') as response:
            response.raise_for_status()
            return await response.json()

    async def refresh(self):
        r = await self.query()
        self.pools = {
            pool["pool_id"].lower(): {
                "base_token": await self.token_db.get(pool["base_currency"].lower()),
                "target_token": await self.token_db.get(pool["target_currency"].lower()), 
            } 
            for pool in r if pool["liquidity_in_usd"] > self.MIN_LIQUIDITY_USD
        }
        logger.debug(f"Refreshed {len(self.pools)} maverick v2 pools")

pool_db = None
pool_db_run_task = None

class MaverickV2Web3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the curve LP through web3."""

    POOL_LENS_CONTRACT_ADDRESS = '0x6A9EB38DE5D349Fe751E0aDb4c0D9D391f94cc8D'
    TIC_NEIGHBORHOOD_SIZE = 5

    def __init__(self, lp_ids, web3_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.web3_client = web3_client

        with open(Path(__file__).parent / 'artifacts' / 'maverick_v2_pool_lens.abi', 'r') as f:
            contract_abi = f.read()
            self.pool_lens = web3_client.eth.contract(
                address=self.POOL_LENS_CONTRACT_ADDRESS,
                abi=contract_abi
            )

    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block("latest")
        return BlockId.from_web3(block)

    async def create_from_blockchain(self, lp_id, block: BlockId) -> MaverickV2:
        block_identifier = block.to_web3()
        lp_id_chksum = self.web3_client.to_checksum_address(lp_id)

        ticks, _, liquidities, sqrt_lower_tick_prices, sqrt_upper_tick_prices, pool_state, sqrt_price, fee01, fee10 = \
            await self.pool_lens.functions.getTicksAroundActiveWLiquidity(
                lp_id_chksum, self.TIC_NEIGHBORHOOD_SIZE
            ).call(block_identifier=block_identifier)

        base_token: Token = pool_db.pools[lp_id]["base_token"]
        quote_token: Token = pool_db.pools[lp_id]["target_token"]   # quote token

        # In univ3 tick i contains prices from sqrt(1.0001)^i to sqrt(1.0001)^(i+1)

        # but in maverick v2, the price intervals are given explicitely in sqrt_lower_tick_prices...sqrt_upper_tick_prices,
        # and assume nr decimals for the price is always 36.
        
        def maverick_sqrt_price_to_univ3_sqrt_price(sqrt_p):
            # Let p be the price in maverick v2, and p' the price in univ3:
            # sqrt(p') * sqrt(10^(-d_q+d_b)) = sqrt(p) * sqrt(10^-36)
            return sqrt_p * 10 ** (-18 + (quote_token.decimals - base_token.decimals) / 2)

        def maverick_tick_index_to_univ3_tick(tick_index):
            return log(maverick_sqrt_price_to_univ3_sqrt_price(sqrt_lower_tick_prices[tick_index]), sqrt(1.0001))

        def index_of_largest_not_greater_than(lst, x):
            for i in reversed(range(len(lst))):
                if lst[i] <= x:
                    return i
            raise ValueError(f"Error finding tick index of maverick v2 pool {lp_id}: {lst}, {x}")

        sqrt_price = maverick_sqrt_price_to_univ3_sqrt_price(sqrt_price)        
        cur_tick_index = index_of_largest_not_greater_than(ticks, pool_state[5])
        cur_tick = maverick_tick_index_to_univ3_tick(cur_tick_index)
        maverick_tick_limit_lb = ticks[0]   # Note: this is in maverick v2 tick space, since it is to be passed to smartcontract
        maverick_tick_limit_ub = ticks[-1]
        ticks = [maverick_tick_index_to_univ3_tick(tick_index) for tick_index in range(len(ticks))]
        univ3_tick_width = log(sqrt_upper_tick_prices[cur_tick_index]/sqrt_lower_tick_prices[cur_tick_index], sqrt(1.0001))
        ticks.append(ticks[-1] + univ3_tick_width)

        def maverick_liquidity_to_univ3_liquidity(l):
            # We solve the following equation for k:
            # l' = l * k
            # sqrt(x * 10^-d_x * y * 10^-d_y) = sqrt(x * 10^-18 * y * 10^-18) * k 
            return l * 10 ** (-18 + (quote_token.decimals + base_token.decimals) / 2)
        
        liquidities = [maverick_liquidity_to_univ3_liquidity(l) for l in liquidities]
        liquidities.append(0)
        liquidity = liquidities[cur_tick_index]
        liquidity_net = {
            ticks[0]: liquidities[0]
        }
        for i in range(1, len(liquidities)):
            liquidity_net[ticks[i]] = liquidities[i] - liquidities[i-1]
        liquidity_net = {k: int(v) for k, v in liquidity_net.items() if int(v) != 0}

        fee01 = fee01 * 1e-18
        fee10 = fee10 * 1e-18

        lp = MaverickV2(
            address=lp_id,
            token0=base_token,
            token1=quote_token,
            sqrt_price=int(sqrt_price * 2**96),
            liquidity=int(liquidity),
            tick=cur_tick,
            liquidity_net=liquidity_net,
            fee01=fee01,
            fee10=fee10,
            tick_limit_lb = maverick_tick_limit_lb, # -cur_tick_index,
            tick_limit_ub = maverick_tick_limit_ub, # len(ticks) - cur_tick_index
        )             
        return lp

    @traced(logger, 'Retrieving maverick v2 state from blockchain.')
    async def __call__(
        self,
        block: BlockId,
        lp_ids: Optional[Set[str]] = None
    ) -> Dict[str, LP]:

        #logger.debug(
        #    f'Retrieving curve state from blockchain at block {block} ...'
        #)

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

        if lp_ids is None:
            lp_ids = self.lp_ids
            
        await asyncio.gather(
            *[add_to_state(lp_id) for lp_id in lp_ids]
        )

        #logger.debug(state)
        return state

class MaverickV2Web3SyncProxy(EventFilteredLPSyncProxyFromAsyncProxy):
    def __init__(self, lp_ids, web3_client, event_stream: EventStream, block_stream: BlockStream):
        async_proxy = MaverickV2Web3AsyncProxy(lp_ids, web3_client)

        with open(Path(__file__).parent / 'artifacts' / 'maverick_v2_pool.abi', 'r') as f:
            contract_abi = f.read()
            Pool = web3_client.eth.contract(
                abi=contract_abi
            )

        events = [
            Pool.events.PoolAddLiquidity, 
            Pool.events.PoolRemoveLiquidity, 
            Pool.events.PoolSetVariableFee, 
            Pool.events.PoolSwap
        ]
        super().__init__(async_proxy, block_stream, lp_ids, events, event_stream)

class MaverickV2Driver(LPDriver):
    def __init__(
        self,
        block_stream: BlockStream,
        event_stream: EventStream,
        session: aiohttp.ClientSession,
        token_db: TokenDB,
        web3_client=None
    ):
        super().__init__(MaverickV2)
        self.block_stream = block_stream
        self.event_stream = event_stream
        self.web3_client = web3_client
        self.session = session
        self.token_db = token_db

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:

        global pool_db
        global pool_db_run_task
        if pool_db is None:
            pool_db = MaverickV2PoolDB(self.session, self.token_db)
            pool_db_run_task = asyncio.create_task(pool_db.run())

        await pool_db.initialized_event.wait() # Wait for the first refresh
        return set(pool_db.pools.keys())
    
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
            sync_proxy = MaverickV2Web3SyncProxy(lp_ids, self.web3_client, self.event_stream, self.block_stream)
        else:
            assert False
        return sync_proxy

    @property
    def uid(self) -> str:
        return f"{self.protocol}-{self.kind}"
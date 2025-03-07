
import asyncio
from copy import deepcopy
import datetime
import logging
from dataclasses import dataclass
from fractions import Fraction as F
from functools import cache
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from itertools import permutations

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy, LPSyncProxy,
                    LPSyncProxyFromAsyncProxy, ProcessedBlockCondition)
from lpbook.error import CacheMissError, TemporaryError
from lpbook.lps.util import DynamicInterval
from lpbook.util import LP, Token, Trade, traced
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from web3.constants import ADDRESS_ZERO
from web3.exceptions import BlockNotFound, ContractLogicError


logger = logging.getLogger(__name__)


@dataclass
class Curve(LP):
    """Curve LP."""
    address: str
    _tokens: List[Token]
    initial_A: F
    future_A: F
    initial_A_time: int
    future_A_time: int
    A_factor: int
    balances: List[int]
    fee: int
    stored_rates: List[int]
    offpeg_fee_multiplier: int
    registry: str
    implementation: str
    name: str
    base_pool_id: Optional[str] = None
    
    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def uid(self) -> str:
        return self.address

    @classmethod
    @property
    def kind(self) -> str:
        return 'Stable'

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Curve'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return ''

    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/1044860 .
        return {
            'mean': 150158.00061890762,
            'stddev': 42372.3387235,
        }

    # old contracts use A'=A*100
    @property
    def A(self) -> F:
        return self.A_helper * self.A_factor

    @property
    def A_helper(self) -> F:
        if self.initial_A == self.future_A:
            return self.initial_A
        timestamp = datetime.datetime.now().timestamp()
        if timestamp >= self.future_A_time:
            return self.future_A
        if timestamp <= self.initial_A_time:
            return self.initial_A
        m = (self.future_A - self.initial_A) / (self.future_A_time - self.initial_A_time)
        return self.initial_A + m * (timestamp - self.initial_A_time)
 
    def xp(self, index) -> int:
        return int(self.stored_rates[index] * self.balances[index] / 10**10)

    def dynamic_fee(self, index1, index2) -> int:
        fee_denom = 10**10
        xp1 = self.xp(index1)
        xp2 = self.xp(index2)
        num = self.fee * self.offpeg_fee_multiplier
        den_1_num = (self.offpeg_fee_multiplier - fee_denom) * 4 * xp1 * xp2
        den_1_den = (xp1 + xp2)**2
        if den_1_den == 0:
            return 0
        return int(num / ((den_1_num / den_1_den) + fee_denom))
       
    @property
    def dynamic_fees(self) -> List[F]:
        return [self.dynamic_fee(i, j) for i, j in permutations(range(len(self.tokens)), 2)]
    
    @property
    def state(self) -> Dict:
        r = {
            'amplification_parameter': self.A,
            'balances': self.balances,
            'fee': F(self.fee, int(1e10)),
        }
        if len(self.stored_rates) > 0:
            r['directional_fees'] = [F(f, int(1e10)) for f in self.dynamic_fees]
            r['scaling_rates'] = [F(int(1e18), s) for s in self.stored_rates]   # FIXME: should be 1e36/s
        return r
    
class CurvePoolDB:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.pools = {}
        self.initialized_event = asyncio.Event()

    async def run(self):
        self.running = True
        await self.refresh()
        self.initialized_event.set()
        while self.running:
            await asyncio.sleep(5*60)
            await self.refresh()

    async def query(self):
        async with self.session.get('https://api.curve.fi/v1/getPools/big/ethereum') as response:
            response.raise_for_status()
            return await response.json()

    async def refresh(self):
        r = await self.query()
        if not r["success"]:
            raise RuntimeError("Failed to query curve pools.")
        self.pools = {pool["address"].lower(): self.parse_pool(pool) for pool in r["data"]["poolData"]}
        logger.debug(f"Refreshed {len(self.pools)} curve pools")

    def parse_pool(self, pool):
        tokens = [self.parse_token(coin) for coin in pool["coins"]]
        balances = [int(coin["poolBalance"]) for coin in pool["coins"]]
        amplification_parameter = int(pool["amplificationCoefficient"])
        return Curve(
            address=pool["address"].lower(), 
            _tokens=tokens, 
            initial_A=amplification_parameter,
            future_A=amplification_parameter,
            initial_A_time=0,
            future_A_time=0, 
            A_factor=1, # we don't know the factor here, must be set later
            balances=balances, 
            fee=None,
            stored_rates=[],
            offpeg_fee_multiplier=None,
            registry=pool["registryId"],
            implementation=pool["implementation"],
            name=pool["name"],
            base_pool_id=pool["basePoolAddress"].lower() if "basePoolAddress" in pool.keys() else None
        )

    def parse_token(self, coin):
        return Token(address=coin["address"].lower(), symbol=coin["symbol"], decimals=int(coin["decimals"]))

curve_pool_db = None
curve_pool_db_run_task = None

class CurveWeb3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the curve LP through web3."""

    REGISTRY_CONTRACT_ADDRESS = '0xF98B45FA17DE75FB1aD0e7aFD971b0ca00e379fC'

    def __init__(self, lp_ids, web3_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.web3_client = web3_client

        with open(Path(__file__).parent / 'artifacts' / 'MetaRegistry.abi', 'r') as f:
            registry_contract_abi = f.read()
            registry_chksum = web3_client.to_checksum_address(
                self.REGISTRY_CONTRACT_ADDRESS
            )
            self.MetaRegistry = web3_client.eth.contract(
                address=registry_chksum,
                abi=registry_contract_abi
            )

        with open(Path(__file__).parent / 'artifacts' / 'StableSwap.abi', 'r') as f:
            contract_abi = f.read()
            self.StableSwap = web3_client.eth.contract(
                abi=contract_abi
            )

        with open(Path(__file__).parent / 'artifacts' / 'StableSwapPlainNG.abi', 'r') as f:
            contract_abi = f.read()
            self.StableSwapPlainNG = web3_client.eth.contract(
                abi=contract_abi
            )

        with open(Path(__file__).parent / 'artifacts' / 'StableSwapMetaNG.abi', 'r') as f:
            contract_abi = f.read()
            self.StableSwapMetaNG = web3_client.eth.contract(
                abi=contract_abi
            )

    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block("latest")
        return BlockId.from_web3(block)

    async def get_fee_from_registry(self, lp_id_chksum, block_identifier) -> int:
        fees = await self.MetaRegistry.functions.get_fees(lp_id_chksum).call(
            block_identifier=block_identifier
        )
        return fees[0]

    async def get_fee_from_pool(self, pool_contract, block_identifier):
        return await pool_contract.functions.fee().call(
            block_identifier=block_identifier
        )

    async def get_dynamic_fee_from_pool(self, lp_id_chksum, Pool, block_identifier, token0_index, token1_index):
        pool_contract = Pool(address=lp_id_chksum)
        return await pool_contract.functions.dynamic_fee(token0_index, token1_index).call(
            block_identifier=block_identifier
        )
    
    async def get_balances(self, lp_id_chksum, block_identifier) -> List[int]:
        return await self.MetaRegistry.functions.get_balances(lp_id_chksum).call(
            block_identifier=block_identifier
        )
    
    async def get_stored_rates(self, pool_contract, block_identifier) -> List[int]:
        return await pool_contract.functions.stored_rates().call(
            block_identifier=block_identifier
        )

    async def get_offpeg_fee_multiplier(self, pool_contract, block_identifier) -> int:
        return await pool_contract.functions.offpeg_fee_multiplier().call(
            block_identifier=block_identifier
        )

    @cache
    def get_contract_for_lp(self, lp_id_chksum, lp_registry, lp_base_pool_id):
        if lp_registry in ["main", "factory"]:
            return self.StableSwap(address=lp_id_chksum)
        elif lp_registry == "factory-stable-ng" and lp_base_pool_id is None:
            return self.StableSwapPlainNG(address=lp_id_chksum)
        elif lp_registry == "factory-stable-ng" and lp_base_pool_id is not None:
            return self.StableSwapMetaNG(address=lp_id_chksum)
        raise RuntimeError("Unknown registry")

    async def set_fees(self, lp_id_chksum, lp, block_identifier):
        if lp.registry in ["main", "factory"]:
            lp.fee = await self.get_fee_from_registry(lp_id_chksum, block_identifier=block_identifier)
        else:
            pool_contract = self.get_contract_for_lp(lp_id_chksum, lp.registry, lp.base_pool_id)
            lp.fee = await self.get_fee_from_pool(pool_contract, block_identifier)
            lp.stored_rates = await self.get_stored_rates(pool_contract, block_identifier)          
            lp.offpeg_fee_multiplier = await self.get_offpeg_fee_multiplier(pool_contract, block_identifier)

    async def set_amplification_parameter(self, lp_id_chksum, lp, block_identifier) -> int:
        pool_contract = self.get_contract_for_lp(lp_id_chksum, lp.registry, lp.base_pool_id)
        lp.future_A = F(await pool_contract.functions.future_A().call(
            block_identifier=block_identifier
        ), 100) # Events send the "precise" (i.e. *100) version of A
        try:
            lp.future_A_time = await pool_contract.functions.future_A_time().call(
                block_identifier=block_identifier
            )
        except ContractLogicError:
            lp.future_A_time = 0
        try:
            lp.initial_A = F(await pool_contract.functions.initial_A().call(
                block_identifier=block_identifier
            ), 100) # Events send the "precise" (i.e. *100) version of A
        except ContractLogicError:
            lp.initial_A = lp.future_A
        try:
            lp.initial_A_time = await pool_contract.functions.initial_A_time().call(
                block_identifier=block_identifier
            )
        except ContractLogicError:
            lp.initial_A_time = lp.future_A_time
        if lp.registry == "factory-stable-ng":
            lp.A_factor = 1
        else:
            # try to guess the factor by checking for the existence of a A_precise() function
            try:
                await pool_contract.functions.A_precise().call(
                    block_identifier=block_identifier
                )
                lp.A_factor = 1
            except ContractLogicError:
                lp.A_factor = 100


    async def set_balances(self, lp_id_chksum, lp, block_identifier) -> List[int]:
        lp.balances = await self.get_balances(lp_id_chksum, block_identifier=block_identifier)
        lp.balances = lp.balances[:len(lp.tokens)]

    async def create_from_blockchain(self, lp_id, block: BlockId) -> Curve:
        block_identifier = block.to_web3()
        lp_id_chksum = self.web3_client.to_checksum_address(lp_id)

        lp = curve_pool_db.pools[lp_id]
        await asyncio.gather(
            self.set_balances(lp_id_chksum, lp, block_identifier),
            self.set_fees(lp_id_chksum, lp, block_identifier),
            self.set_amplification_parameter(lp_id_chksum, lp, block_identifier)
        )
        return lp

    @traced(logger, 'Retrieving curve state from blockchain.')
    async def __call__(
        self,
        block: BlockId
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

        await asyncio.gather(
            *[add_to_state(lp_id) for lp_id in self.lp_ids]
        )

        #logger.debug(state)
        return state


class CurveWeb3SyncProxy(LPFromInitialStatePlusChangesProxy):
    def __init__(self, async_proxy, event_stream, block_stream: Optional[BlockStream], web3_client, registry):
        self.web3_client = web3_client
        self.block_stream = block_stream
        self.registry = registry
        if registry == "factory-stable-ng":
            StableSwap = async_proxy.StableSwapPlainNG
        else:
            StableSwap = async_proxy.StableSwap

        # I gave up trying to keep up with balances incrementally, so the balances are re-read each update, via the
        # extra updater mechanism below.
        # The only reason we still subsribe to the TokenExchange event is for get_trades().
        events = [
            StableSwap.events.TokenExchange, 
            #StableSwap.events.AddLiquidity, 
            #StableSwap.events.RemoveLiquidity,
            #StableSwap.events.RemoveLiquidityOne,
            #StableSwap.events.RemoveLiquidityImbalance,
            StableSwap.events.RampA,
            StableSwap.events.StopRampA,
        ]
        # Although there are different contracts for plan and meta NG pools, they share the same events.
        if registry == "factory-stable-ng":
            events.append(StableSwap.events.ApplyNewFee)
        else:
            events.append(StableSwap.events.NewFee)
            events.append(StableSwap.events.NewParameters)  # really old pools, e.g. 0xa5407eae9ba41422680e2e00537571bcc53efbfd
         
        super().__init__(
            async_proxy.lp_ids,
            events,
            async_proxy,
            event_stream,
            web3_client
        )

        self.next_fetch_block_by_lp_id = {}
        self.fetch_interval_by_lp_id = {}
        self.initialized_lps_with_dynamic_rates = False
        self.latest_dynamic_rates_by_lp_id = {}
        self.processed_block_cond = None
        
    async def start(self) -> None:
        if self.block_stream is not None:
            self.block_stream.subscribe(self.on_new_block)
        await super().start()
    
    async def stop(self) -> None:
        if self.block_stream is not None:
            self.block_stream.unsubscribe(self.on_new_block)
        await super().stop()

    # As crazy as it sounds it seems the contract does not say which tokens have dynamic rates. This hack checks
    # that by looking for rates that are not powers of 10.
    def is_dynamic_rate(self, rate):
        return math.log10(rate) != int(math.log10(rate))
    
    async def on_new_block(self, block: BlockId) -> None:
        if self.checkpoint is None:
            return
        if self.processed_block_cond is None:
            self.processed_block_cond = ProcessedBlockCondition()
        if not self.initialized_lps_with_dynamic_rates:
            # Check if new pools with dynamic rates are available
            for lp_id, lp in self.checkpoint.items():
                has_dynamic_rate = any([self.is_dynamic_rate(rate) for rate in lp.stored_rates])
                if not has_dynamic_rate:
                    continue
                self.next_fetch_block_by_lp_id[lp_id] = block.number
                self.fetch_interval_by_lp_id[lp_id] = DynamicInterval(1, 60, increase_factor=1.1, decrease_factor=float("inf"))
            self.initialized_lps_with_dynamic_rates = True
        lp_ids_to_fetch = [
            lp_id 
            for lp_id, next_fetch_block in self.next_fetch_block_by_lp_id.items()
            if block.number >= next_fetch_block
        ]
        if len(lp_ids_to_fetch) > 0:
            await asyncio.gather(*[self.fetch_dynamic_rate(lp_id, block) for lp_id in lp_ids_to_fetch])

        await self.processed_block_cond.on_block_processed(block)

    async def fetch_dynamic_rate(self, lp_id: str, block: BlockId):
        # Fetch the rates.
        lp = self.checkpoint[lp_id]
        lp_id_chksum = self.web3_client.to_checksum_address(lp_id)
        pool_contract = self.async_proxy.get_contract_for_lp(lp_id_chksum, lp.registry, lp.base_pool_id)
        new_stored_rates = await self.async_proxy.get_stored_rates(pool_contract, "latest")
        new_rates = new_stored_rates

        # Update fetch intervals.
        if lp_id in self.latest_dynamic_rates_by_lp_id.keys():
            if new_rates != self.latest_dynamic_rates_by_lp_id[lp_id]:
                self.fetch_interval_by_lp_id[lp_id].decrease()
            else:
                self.fetch_interval_by_lp_id[lp_id].increase()
        self.next_fetch_block_by_lp_id[lp_id] = block.number + self.fetch_interval_by_lp_id[lp_id].cur_interval

        # Update the rates. 
        if lp_id in self.latest_dynamic_rates_by_lp_id and new_rates != self.latest_dynamic_rates_by_lp_id[lp_id]:
            logger.debug(f"New curveng rates for lp {lp_id}: {new_rates}. Refetching in {self.fetch_interval_by_lp_id[lp_id].cur_interval} blocks.")

        self.latest_dynamic_rates_by_lp_id[lp_id] = new_rates

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""

        lp_id = d.address.lower()
        if lp_id not in state.keys():
            return
        lp = state[lp_id]

        # I gave up trying to keep up with balances incrementally, so the balances are re-read each update, via the
        # extra updater mechanism below.

        #if d.event == 'TokenExchange':
        #    lp.balances[d.args.sold_id] += d.args.tokens_sold  # pool bought
        #    lp.balances[d.args.bought_id] -= d.args.tokens_bought # pool sold
        #elif d.event == 'AddLiquidity':
        #    for i in range(len(lp.balances)):
        #        lp.balances[i] += d.args.token_amounts[i]
        #elif d.event in ['RemoveLiquidity', 'RemoveLiquidityImbalance']:
        #    for i in range(len(lp.balances)):
        #        lp.balances[i] -= d.args.token_amounts[i]
        #elif d.event == 'RemoveLiquidityOne':
        #    # old pools don't say which token was removed (!), so these are updated via
        #    # the extra updater mechanism below.
        #    if "token_id" not in d.args:
        #        return
        #    lp.balances[d.args.token_id] -= d.args.coin_amount
        if d.event == 'RampA':
            lp.initial_A = d.args.old_A
            lp.future_A = d.args.new_A
            lp.initial_A_time = d.args.initial_time
            lp.future_A_time = d.args.future_time
        elif d.event == 'StopRampA':
            lp.initial_A = lp.future_A = d.args.A
            lp.initial_A_time = lp.future_A_time = d.args.t
        elif d.event == "ApplyNewFee":      # curve-ng
            lp.fee = d.args.fee
            lp.offpeg_fee_multiplier = d.args.offpeg_fee_multiplier
        elif d.event == "NewFee":           # curve-old
            lp.fee = d.args.fee
        elif d.event == "NewParameters":    # curve-very-old
            lp.fee = d.args.fee
            lp.initial_A = lp.future_A = d.args.A

        if lp_id in self.latest_dynamic_rates_by_lp_id.keys():
            lp.stored_rates = self.latest_dynamic_rates_by_lp_id[lp_id]

    async def on_sync(self, events, block: BlockId) -> None:
        if self.checkpoint is None:
            return
        events = [
            event for event in events 
            if event.event in {'RemoveLiquidityOne', 'TokenExchange', 'AddLiquidity', 'RemoveLiquidity', 'RemoveLiquidityImbalance'}
        ]
        if len(events) > 0:
            updaters = await asyncio.gather(*[self.create_balances_updater(event) for event in events])
            for updater, event in zip(updaters, events):
                if updater is not None:
                    self.add_event_updater(event, updater)

        if self.processed_block_cond is not None:
            await self.processed_block_cond.wait_for_block(block)

    async def create_balances_updater(self, event):
        lp_id = event.address.lower()
        lp_id_chksum = self.web3_client.to_checksum_address(lp_id)
        block_identifier = event.blockHash
        new_balances = await self.async_proxy.get_balances(lp_id_chksum, block_identifier)
        def updater(state):
            state[lp_id].balances = new_balances[:len(state[lp_id].tokens)]
        return updater

    def get_trades(self, prev_state: Dict[str, LP], changes: List[Any]) -> list[Trade]:
        """Assembles list of trades from updates."""
        trades = []

        cur_state = deepcopy(prev_state)

        for d in changes:
            lp_id = d.address.lower()
            if lp_id not in cur_state.keys():
                continue
            lp = cur_state[lp_id]

            if d.event != 'TokenExchange':
                continue
            buy_token_index = d.args.sold_id
            sell_token_index = d.args.bought_id
            buy_amount = d.args.tokens_sold
            sell_amount = d.args.tokens_bought

            trade = Trade(
                lp_id=lp_id,
                block_number=d.blockNumber,
                token1=lp.tokens[buy_token_index],
                token2=lp.tokens[sell_token_index],
                buy_amount1=buy_amount, 
                buy_amount2=-sell_amount,
            )
            trades.append(trade)

        return trades
    
# This driver supports the old curve pools. It uses an async web3 proxy to query the state of the pools. 
class CurveDriver(LPDriver):
    def __init__(
        self,
        event_stream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(Curve)
        self.event_stream = event_stream
        self.web3_client = web3_client
        self.session = session

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
            async_proxy = CurveWeb3AsyncProxy(lp_ids, self.web3_client)
        else:
            assert False
        #sync_proxy = LPSyncProxyFromAsyncProxy(
        #    async_proxy, self.block_stream
        #)
        sync_proxy = CurveWeb3SyncProxy(
            async_proxy, self.event_stream, None, self.web3_client, "main"
        )
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:

        global curve_pool_db
        global curve_pool_db_run_task
        if curve_pool_db is None:
            curve_pool_db = CurvePoolDB(self.session)
            curve_pool_db_run_task = asyncio.create_task(curve_pool_db.run())

        await curve_pool_db.initialized_event.wait() # Wait for the first refresh

        DENYLIST = [
            # Can't interact with these pools
            '0x80466c64868e1ab14a1ddf27a676c3fcbe638fe5',   # Looks like an old cryptopool
            '0x4e0915c88bc70750d68c481540f081fefaf22273',
            '0x1005f7406f32a61bd760cfa14accd2737913d546',
            '0x0ce6a5ff5217e38315f87032cf90686c96627caa',
            '0xd51a44d3fae010294c616388b506acda1bfaae46',
            '0x98a7f18d4e56cfe84e3d081b40001b3d5bd3eb8b',
            '0xf92f430dd8567b0d466358c79594ab58d919a6d4'            
        ]

        #print("tokens:", {token.address for lp in curve_pool_db.pools for token in lp.tokens})
        return [
            lp.address 
            for lp in curve_pool_db.pools.values() 
            if len({token.address for token in lp.tokens} & set(token_ids)) >= 2 and
            lp.registry in ["main", "factory"] and
            #lp.base_pool_id is None and
            lp.address not in DENYLIST
        ]

    @property
    def uid(self) -> str:
        return f"{self.protocol}-{self.kind}-main"
    
# This driver supports the new curve pools. It uses an sync web3 proxy to query the state of the pools.
class CurveNGDriver(LPDriver):
    def __init__(
        self,
        event_stream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(Curve)
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.session = session

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
            async_proxy = CurveWeb3AsyncProxy(lp_ids, self.web3_client)
        else:
            assert False
        sync_proxy = CurveWeb3SyncProxy(
            async_proxy, self.event_stream, self.block_stream, self.web3_client, "factory-stable-ng"
        )
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:

        global curve_pool_db
        global curve_pool_db_run_task
        if curve_pool_db is None:
            curve_pool_db = CurvePoolDB(self.session)
            curve_pool_db_run_task = asyncio.create_task(curve_pool_db.run())
        
        await curve_pool_db.initialized_event.wait() # Wait for the first refresh

        DENYLIST = []

        #print("tokens:", {token.address for lp in curve_pool_db.pools for token in lp.tokens})
        return [
            lp.address 
            for lp in curve_pool_db.pools.values() 
            if len({token.address for token in lp.tokens} & set(token_ids)) >= 2 and
            all(token.address != "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" for token in lp.tokens) and
            lp.registry in ["factory-stable-ng"] and
            lp.address not in DENYLIST
        ]
    
    @property
    def uid(self) -> str:
        return f"{self.protocol}-{self.kind}-NG"
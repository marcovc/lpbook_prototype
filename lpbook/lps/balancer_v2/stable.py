
import asyncio
from dataclasses import dataclass
import datetime
import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from async_lru import alru_cache

from lpbook import LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy, LPSyncProxy, LPSyncProxyFromAsyncProxy, MultiLPFromInitialStatePlusChangesProxy
from lpbook.error import TemporaryError
from lpbook.lps.balancer_v2.common import BalancerV2BalancesWeb3SyncProxy, BalancerV2FeesWeb3SyncProxy
from lpbook.lps.balancer_v2.subgraph import BalancerV2GraphQLClient
from lpbook.lps.util import DynamicInterval
from lpbook.util import LP, Token, traced
from fractions import Fraction as F

from lpbook.web3 import BlockId, TokenDB
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream
from web3.exceptions import ContractLogicError, BlockNotFound
from dotenv import load_dotenv
import aiohttp

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")

logger = logging.getLogger(__name__)

def lp_id_to_address(lp_id) -> str:
    return lp_id[:42]

def lp_id_to_checksum_address(lp_id, w3) -> str:
    return w3.to_checksum_address(lp_id_to_address(lp_id))

# Note: These pools include the LP token as part of the tokens list. However, the rules
# for trading with this token seem unrelated with the stableswap math, see
# https://github.com/balancer/balancer-v2-monorepo/blob/master/pkg/pool-stable/contracts/ComposableStablePool.sol#L49-L51,
# so it is excluded from the tokens list sent to the solver.
@dataclass
class ComposableStableV2(LP):
    """ComposableStableV2 LP."""
    _id: str
    all_tokens: List[Token]
    initial_A: F
    future_A: F 
    initial_A_time: int
    future_A_time: int
    A_factor: int
    balances: List[int]
    fee: F
    stored_rates: List[int]
    stored_rates_expiry: List[int]
    stored_rates_duration: List[int]

    owner: str

    def exclude_pool_token(self, l):
        return [b for b, t in zip(l, self.all_tokens) if t.address != lp_id_to_address(self._id)]

    # Note: excluding pool token, see note above.
    @property
    def tokens(self) -> List[Token]:
        return self.exclude_pool_token(self.all_tokens)

    @property
    def uid(self) -> str:
        return self._id

    @classmethod
    @property
    def kind(self) -> str:
        return 'Stable'

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Balancer'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'

    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/1044860 .
        return {
            'mean': 88000,
            'stddev': 42372.3387235,
        }

    @property
    def address(self) -> str:
        return lp_id_to_address(self._id)
    
    @property
    def A(self) -> F:
        if self.initial_A == self.future_A:
            return self.initial_A
        timestamp = datetime.datetime.now().timestamp()
        if timestamp >= self.future_A_time:
            return self.future_A
        if timestamp <= self.initial_A_time:
            return self.initial_A
        m = (self.future_A - self.initial_A) / (self.future_A_time - self.initial_A_time)
        return self.initial_A + m * (timestamp - self.initial_A_time)
 
    # Immutable, set at contract creation.
    def scaling_factor(self, index) -> int:
        return 10**(36-self.all_tokens[index].decimals)
    
    @property
    def scaling_factors_times_rates(self) -> List[F]:
        return [F(self.scaling_factor(index), 10**18) * F(self.stored_rates[index], 10**18) for index in range(len(self.all_tokens))]

    @property
    def fee_discount_factor(self) -> Optional[F]:
        if self.owner != "0xba1ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1b":
            return None
        # Applying 80% discount in bounty
        return F(20, 100)
    
    @property
    def state(self) -> Dict:
        fee = self.fee
        if self.fee_discount_factor is not None:
            fee *= self.fee_discount_factor
        r = {
            'amplification_parameter': self.A ,
            'balances': self.exclude_pool_token(self.balances),
            'fee': fee,    
            'scaling_rates': self.exclude_pool_token([10**18 / factor_times_rate for factor_times_rate in self.scaling_factors_times_rates]),
        }
        return r

    @property
    def execution_info(self):
        r = {}
        if self.fee_discount_factor is not None:
            r['fee_discount_factor'] = self.fee_discount_factor     # to issue the required set/unset fee contract calls
        return r


class BalancerV2Web3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the balancer v2 LP through web3."""
    vault_address = "0xba12222222228d8ba445958a75a0704d566bf2c8"
    AMP_SLOT = 9
    AMP_START_VALUE_MASK = (1 << 64) - 1  # 0xFFFFFFFFFFFFFFFF
    AMP_END_VALUE_MASK = (1 << 64) - 1    # 0xFFFFFFFFFFFFFFFF
    AMP_TIMESTAMP_MASK = (1 << 64) - 1    # 0xFFFFFFFFFFFFFFFF

    def __init__(self, lp_ids, web3_client, token_db: TokenDB):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.web3_client = web3_client
        self.token_db = token_db

        with open(Path(__file__).parent / 'artifacts' / 'Vault.abi', 'r') as f:
            vault_abi = f.read()
            vault_address_chksum = self.web3_client.to_checksum_address(self.vault_address)
            self.Vault = web3_client.eth.contract(
                address=vault_address_chksum,
                abi=vault_abi
                )

        self.ComposableStablePool = {} 
        with open(Path(__file__).parent / 'artifacts' / 'ComposableStablePool.abi', 'r') as f:
            abi = f.read()
            for lp_id in lp_ids:
                address_chksum = lp_id_to_checksum_address(lp_id, self.web3_client)
                self.ComposableStablePool[lp_id] = web3_client.eth.contract(
                    address=address_chksum,
                    abi=abi
                )

    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block("latest")
        return BlockId.from_web3(block)

    async def get_amp_data(self, lp_id, block_identifier):
        address = lp_id_to_checksum_address(lp_id, self.web3_client)
        slot_raw_data = await self.web3_client.eth.get_storage_at(address, self.AMP_SLOT, block_identifier)
        packed_data = int.from_bytes(slot_raw_data, byteorder="big")
        # Start value (bits 0-63)
        start_value = packed_data & self.AMP_START_VALUE_MASK
        # End value (bits 64-127)
        end_value = (packed_data >> 64) & self.AMP_END_VALUE_MASK
        # Start time (bits 128-191)
        start_time = (packed_data >> 128) & self.AMP_TIMESTAMP_MASK
        # End time (bits 192-255)
        end_time = (packed_data >> 192) & self.AMP_TIMESTAMP_MASK
        return (start_value, end_value, start_time, end_time)

    async def get_amp_factor(self, lp_id, block_identifier):
        _, _, precision = await self.ComposableStablePool[lp_id].functions.getAmplificationParameter().call(
            block_identifier=block_identifier
        )
        return precision
    
    async def get_cached_rate_data(self, lp_id, token_addresses, block_identifier):
        rates = []
        expiries = []
        durations = []
        for token_address in token_addresses:
            try:
                rate, _, duration, expiry = await self.ComposableStablePool[lp_id].functions.getTokenRateCache(token_address).call(
                    block_identifier=block_identifier
                )
            except ContractLogicError:
                rate = int(1e18)
                expiry = float('inf')
                duration = float('inf')
            rates.append(rate)
            expiries.append(expiry)
            durations.append(duration)
        return rates, expiries, durations

    async def create_from_blockchain(self, lp_id, block: BlockId) -> Optional[ComposableStableV2]:
        block_identifier = block.to_web3()

        tokens, balances, _ = await self.Vault.functions.getPoolTokens(lp_id).call(
            block_identifier=block_identifier
        )
        initial_A, future_A, initial_A_time, future_A_time = await self.get_amp_data(lp_id, block_identifier)
        A_factor = await self.get_amp_factor(lp_id, block_identifier)

        fee_e18 = await self.ComposableStablePool[lp_id].functions.getSwapFeePercentage().call(
            block_identifier=block_identifier
        )
        owner = await self.ComposableStablePool[lp_id].functions.getOwner().call(
            block_identifier=block_identifier
        )
        owner = owner.lower()
        stored_rates, stored_rates_expiry, stored_rates_duration = await self.get_cached_rate_data(lp_id, tokens, block_identifier)

        tokens = [await self.token_db.get(token) for token in tokens]

        if any(token is None for token in tokens):
            return None
        
        balances = [int(balance) for balance in balances]

        return ComposableStableV2(
            _id=lp_id,
            all_tokens=tokens,
            initial_A=F(initial_A, A_factor),
            future_A=F(future_A, A_factor),
            initial_A_time=initial_A_time,
            future_A_time=future_A_time,
            A_factor=A_factor,
            balances=balances,
            fee=F(fee_e18, int(1e18)),        
            stored_rates=stored_rates,
            stored_rates_expiry=stored_rates_expiry,
            stored_rates_duration=stored_rates_duration,
            owner=owner
        )

    @alru_cache(maxsize=128)
    @traced(logger, 'Retrieving stable balancer v2 state from blockchain')
    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        state = {}

        async def add_to_state(lp_id):
            try:
                pool = await self.create_from_blockchain(
                    lp_id,
                    block
                )
                if pool is not None:
                    state[lp_id] = pool
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


# Tracks A and stored rates state.
class BalancerV2AmpAndStoredRatesWeb3SyncProxy(LPFromInitialStatePlusChangesProxy):

    def __init__(self, lp_ids, async_proxy, event_stream, block_stream, web3_client):
        self.web3_client = web3_client
        self.async_proxy = async_proxy
        self.block_stream = block_stream
        with open(Path(__file__).parent / 'artifacts' / 'ComposableStablePool.abi', 'r') as f:
            abi = f.read()
            self.ComposableStablePool = web3_client.eth.contract(
                abi=abi
            )

        events = [
            self.ComposableStablePool.events.AmpUpdateStarted, 
            self.ComposableStablePool.events.AmpUpdateStopped, 
            self.ComposableStablePool.events.TokenRateCacheUpdated,
            self.ComposableStablePool.events.TokenRateProviderSet
        ]
         
        lp_addresses = [lp_id_to_address(lp_id) for lp_id in lp_ids]
        super().__init__(
            lp_addresses,
            events,
            async_proxy,
            event_stream,
            web3_client
        )
        self.updated_stored_rates = {}
        self.fetch_interval_by_lp_id_and_token_index = {}
        self.next_fetch_block_by_lp_id_and_token_index = {}
        self.block_stream.subscribe(self.on_new_block)

    def __del__(self):
        self.block_stream.unsubscribe(self.on_new_block)

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""

        # if there are any pending updated rates, apply them now, irrespective of the event.
        for lp_id, updated_rates in self.updated_stored_rates.items():
            state[lp_id].stored_rates = updated_rates
        self.updated_stored_rates.clear()

        # Now process the event as usual.
        lp_id = d.address.lower()
        if lp_id not in state.keys():
            return
        lp = state[lp_id]

        if d.event == 'AmpUpdateStarted':
            lp.initial_A = F(d.args.startValue, lp.A_factor)
            lp.future_A = F(d.args.endValue, lp.A_factor)
            lp.initial_A_time = d.args.startTime
            lp.future_A_time = d.args.endTime
        elif d.event == 'AmpUpdateStopped':
            lp.initial_A = lp.future_A = F(d.args.currentValue, lp.A_factor)
            lp.initial_A_time = lp.future_A_time = datetime.datetime.now().timestamp()
        elif d.event == 'TokenRateCacheUpdated':
            lp.stored_rates[d.args.tokenIndex] = d.args.rate
        elif d.event == 'TokenRateProviderSet':
            lp.stored_rates_expiry[d.args.tokenIndex] = d.args.duration + datetime.datetime.now().timestamp()
            lp.stored_rates_duration[d.args.tokenIndex] = d.args.duration
        else:
            assert False

    # Bypasses cache.
    async def get_rate(self, lp_id, token: Token) -> int:
        token_address = self.web3_client.to_checksum_address(token.address)
        return await self.async_proxy.ComposableStablePool[lp_id].functions.getTokenRate(token_address).call()

    async def on_new_block(self, block: BlockId) -> None:
        if self.checkpoint is None:
            return

        now = datetime.datetime.now()

        def stored_rates_have_likely_changed(lp, token_index):
            if (lp.uid, token_index) not in self.next_fetch_block_by_lp_id_and_token_index:
                return True
            return block.number >= self.next_fetch_block_by_lp_id_and_token_index[lp.uid, token_index]
            
        # Only update rates of pools whose rate has changed in the last 15 days,
        # that will not default to the cached rate if used in this block,
        # and that whose rate has likely changed.
        MAX_POOL_AGE_TO_UPDATE = (now - datetime.timedelta(days=15)).timestamp()
        lp_tokens_index_to_update = [
            (lp, i)
            for lp in self.checkpoint.values()
            for i in range(len(lp.all_tokens))
            if MAX_POOL_AGE_TO_UPDATE < lp.stored_rates_expiry[i] < now.timestamp() and
            stored_rates_have_likely_changed(lp, i)
        ]

        if len(lp_tokens_index_to_update) == 0:
            return

        async def update_lp_token_rate(lp, token_index):
            old_rate = self.updated_stored_rates.get(lp.uid, lp.stored_rates)[token_index]
            new_rate = await self.get_rate(lp.uid, lp.all_tokens[token_index])
            self.updated_stored_rates[lp.uid] = self.updated_stored_rates.get(lp.uid, lp.stored_rates[:])
            self.updated_stored_rates[lp.uid][token_index] = new_rate

            if (lp.uid, token_index) not in self.fetch_interval_by_lp_id_and_token_index:
                self.fetch_interval_by_lp_id_and_token_index[(lp.uid, token_index)] = DynamicInterval(1, 60, increase_factor=1.1, decrease_factor=float("inf"))
            
            if old_rate == new_rate:
                self.fetch_interval_by_lp_id_and_token_index[(lp.uid, token_index)].increase()
            else:
                self.fetch_interval_by_lp_id_and_token_index[(lp.uid, token_index)].decrease()

            self.next_fetch_block_by_lp_id_and_token_index[lp.uid, token_index] = block.number + self.fetch_interval_by_lp_id_and_token_index[(lp.uid, token_index)].cur_interval

            #print(f"Updated rate for {lp.uid} token {token_index} to {new_rate} at block {block.number}. Next fetch at {self.next_fetch_block_by_lp_id_and_token_index[lp.uid, token_index]}")

        await asyncio.gather(
            *[update_lp_token_rate(lp, token_index) for lp, token_index in lp_tokens_index_to_update]
        )


class BalancerV2Driver(LPDriver)    :
    def __init__(
        self,
        token_db: TokenDB,
        event_stream: EventStream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
)   :
        super().__init__(ComposableStableV2)
        self.token_db = token_db
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/C4ayEZP2yTXRAB8vSaTrgN4m9anTe9Mdm2ViyiAuV9TV'
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.graphql_client = BalancerV2GraphQLClient(self.thegraph_url, session)

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        async_proxy = BalancerV2Web3AsyncProxy(
            lp_ids, self.web3_client, self.token_db
        )
        #sync_proxy = LPSyncProxyFromAsyncProxy(
        #    async_proxy, self.block_stream
        #)
        #return sync_proxy
        
        sync_proxy_1 = BalancerV2BalancesWeb3SyncProxy(lp_ids, async_proxy, self.event_stream, self.web3_client)
        sync_proxy_2 = BalancerV2FeesWeb3SyncProxy(lp_ids, async_proxy, self.event_stream, self.web3_client) 
        sync_proxy_3 = BalancerV2AmpAndStoredRatesWeb3SyncProxy(lp_ids, async_proxy, self.event_stream, self.block_stream, self.web3_client)

        return MultiLPFromInitialStatePlusChangesProxy([sync_proxy_1, sync_proxy_2, sync_proxy_3])

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        def is_valid_pool(pool):
            return (
                float(pool.total_liquidity) >= 1000 and  # USD
                pool.pool_type == 'ComposableStable' and 
                pool.swap_enabled and
                not pool.is_paused
            )

        ids = [
            pool.id
            for pool in await self.graphql_client.get_pools_containing_tokens(token_ids)
            if is_valid_pool(pool)
        ]
        return ids


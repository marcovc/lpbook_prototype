
import asyncio
import logging
from dataclasses import dataclass
from fractions import Fraction as F
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from async_lru import alru_cache

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver,
                    LPSyncProxy, LPSyncProxyFromAsyncProxy)
from lpbook.lps.balancer_v2.weighted import BalancerV2
from lpbook.lps.balancer_v3.common import BalancerV3BalancesAndFeesWeb3SyncProxy
from lpbook.lps.balancer_v3.subgraph import BalancerV3GraphQLClient
from lpbook.util import LP, ExchangeRate, Token, Trade, traced
from lpbook.web3 import BlockId, TokenDB
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream
from lpbook.error import TemporaryError
from web3.exceptions import BlockNotFound, ContractLogicError

from dotenv import load_dotenv
import os

load_dotenv()

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))

logger = logging.getLogger(__name__)


# Currently only supports Weighted type.

@dataclass
class BalancerV3(BalancerV2):
    """Balancer V3."""

    @property
    def state(self) -> Dict:
        fee = F(self.fee_e18, int(1e18))
        return {
            'type': self.type,
            'balances': self.balances,
            'weights': self.weights,
            'fee': fee, 
        }

    @property
    def execution_info(self):
        return {}
    
    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'

    @property
    def gas_stats(self) -> Dict:
        return {
            'mean': 88892, 
            'stddev': 0
        }

    @property
    def address(self) -> str:
        return self._id

# Too laggy to be useful (usually 3 blocks behind)
class BalancerV3TheGraphAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the balancer v3 LP through TheGraph."""
    def __init__(self, lp_ids, balancer_v3_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = balancer_v3_gql_client

    def create_from_graphql(self, graph_data) -> BalancerV3:
        tokens = [
            Token(
                address=token.address,
                symbol=token.symbol,
                decimals=int(token.decimals)
            )
            for token in graph_data.pool_tokens
        ]
        balances = [
            int(D(token.balance) * 10**int(token.decimals))
            for token in graph_data.pool_tokens
        ]
        weights = [
            D(token.weight) for token in graph_data.pool_tokens
        ]
        lp_id = graph_data.id

        return BalancerV3(
            _id=lp_id,
            all_tokens=tokens,
            balances=balances,
            weights=weights,
            fee_e18=int(D(graph_data.dynamic_data.swap_fee) * D(1e18)),
            type="Weighted",
            owner=graph_data.swap_fee_manager.lower()   # not sure this is the right field
        )

    async def latest_block(self) -> BlockId:
        block_number = await self.client.get_last_block_number()
        return BlockId(number = block_number)

    @alru_cache(maxsize=128)
    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:
        logger.debug(
            f'Retrieving balancer v3 state from TheGraph at block {block} ...'
        )

        # It seems balancer graph needs a bit to sync after the new block is announced.
        if block.number is not None:
            while True:
                latest_block_number = (await self.latest_block()).number
                if block.number <= latest_block_number:
                    break
                logger.debug(
                    f'{self} is lagging behind '
                    f'{block.number - latest_block_number} blocks. Retrying ...'
                )
                await asyncio.sleep(2)

        lp_filter = {
            'id_in': self.lp_ids
        }
        graph_data = [
            pool
            async for pool in self.client.get_pools_state(lp_filter, None)
        ]
        state = {
            pool.id: self.create_from_graphql(pool)
            for pool in graph_data
        }

        #logger.debug(state)
        return state

class BalancerV3Web3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the balancer v3 LP through web3."""
    def __init__(self, lp_ids, web3_client, token_db: TokenDB):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.w3_client = web3_client
        self.token_db = token_db

        self.WeightedPool = {} 
        with open(Path(__file__).parent / 'artifacts' / 'WeightedPool.abi', 'r') as f:
            weighted_pool_abi = f.read()
            for lp_id in lp_ids:
                address = lp_id
                address_chksum = self.w3_client.to_checksum_address(address)
                self.WeightedPool[lp_id] = web3_client.eth.contract(
                    address=address_chksum,
                    abi=weighted_pool_abi
                )

    async def latest_block(self) -> BlockId:
        block = await self.w3_client.eth.get_block("latest")
        return BlockId.from_web3(block)

    async def create_from_blockchain(self, lp_id, block: BlockId) -> Optional[BalancerV2]:
        block_identifier = block.to_web3()

        async with asyncio.TaskGroup() as tg:
            get_pool_tokens = tg.create_task(
                self.WeightedPool[lp_id].functions.getTokenInfo().call(
                    block_identifier=block_identifier
                )
            )
            get_normalized_weights = tg.create_task(
                self.WeightedPool[lp_id].functions.getNormalizedWeights().call(
                    block_identifier=block_identifier
                )
            )
            get_aggregate_fee_percentages = tg.create_task(
                self.WeightedPool[lp_id].functions.getAggregateFeePercentages().call(
                    block_identifier=block_identifier
                )
            )
            #get_owner = tg.create_task(
            #    self.WeightedPool[lp_id].functions.getOwner().call(
            #        block_identifier=block_identifier
            #    )
            #)
        
        tokens, _, balances, _ = get_pool_tokens.result()
        weights = [str(w * 1e-18) for w in get_normalized_weights.result()]
        swap_fee_e18, _ = get_aggregate_fee_percentages.result()
        #owner = get_owner.result().lower()

        tokens = await asyncio.gather(*[self.token_db.get(token) for token in tokens])

        if any(token is None for token in tokens):
            return None
        
        balances = [int(balance) for balance in balances]

        return BalancerV3(
            _id=lp_id,
            all_tokens=tokens,
            balances=balances,
            weights=weights,
            fee_e18=swap_fee_e18,        
            type="Weighted",
            owner=None
        )

    @alru_cache(maxsize=128)
    @traced(logger, "Retrieving balancer v3 state from blockchain")
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

        logger.debug(state)
        return state


    
class BalancerV3Driver(LPDriver):
    def __init__(
        self,
        token_db: TokenDB,
        event_stream: EventStream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(BalancerV3)
        self.token_db = token_db
        self.graphql_url = f'https://api-v3.balancer.fi/'
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.graphql_client = BalancerV3GraphQLClient(self.graphql_url, session)

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        if data_source in [
            #LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        ]:
            async_proxy = BalancerV3TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        elif data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.Web3
        ]:
            async_proxy = BalancerV3Web3AsyncProxy(
                lp_ids, self.web3_client, self.token_db
            )
        elif data_source == LPDriver.LPSyncProxyDataSource.TheGraph:
            async_proxy = BalancerV3TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
            sync_proxy = LPSyncProxyFromAsyncProxy(
                async_proxy, self.block_stream
            )
            return sync_proxy
        else:
            assert False # No other proxies are currently implemented for balancer.
        
        sync_proxy = BalancerV3BalancesAndFeesWeb3SyncProxy(lp_ids, async_proxy, self.event_stream, self.web3_client)
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
            
        ids = [
            pool.id
            for pool in await self.graphql_client.get_pools_containing_tokens(token_ids, ["WEIGHTED"], 1000)
        ]
        return ids



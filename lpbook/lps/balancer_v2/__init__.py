
import asyncio
from copy import deepcopy
import logging
from dataclasses import dataclass
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from pathlib import Path
from typing import Any, Dict, List

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy,
                    LPSyncProxy, LPSyncProxyFromAsyncProxy)
from lpbook.lps.balancer_v2.subgraph import BalancerV2GraphQLClient
from lpbook.util import LP, Token
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))

logger = logging.getLogger(__name__)

# NOTE: This is not properly debugged because there is not enough action on balancer lately.
# It seems Balancer stable pools have more swaps.

@dataclass
class BalancerV2(LP):
    """Balancer V2."""
    _id: str
    _tokens: List[Token]
    balances: List[int]
    weights: List[str]
    fee: float
    type: str

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def uid(self) -> str:
        return self._id

    @property
    def state(self) -> Dict:
        return {
            'type': self.type,
            'balances': self.balances,
            'weights': self.weights,
            'fee': self.fee,
        }

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Balancer'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'

    @classmethod
    @property
    def gas_stats(self) -> Dict:
        return {
            'mean': 88892, 
        }


class BalancerV2TheGraphAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the balancer v2 LP through TheGraph."""
    def __init__(self, lp_ids, balancer_v2_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = balancer_v2_gql_client

    def create_from_thegraph(self, thegraph_data) -> BalancerV2:
        tokens = [
            Token(
                address=token.address,
                symbol=token.symbol,
                decimals=int(token.decimals)
            )
            for token in thegraph_data.tokens
        ]
        balances = [
            int(D(token.balance) * 10**int(token.decimals))
            for token in thegraph_data.tokens
        ]
        weights = [
            token.weight for token in thegraph_data.tokens
        ]

        return BalancerV2(
            _id=thegraph_data.id,
            _tokens=tokens,
            balances=balances,
            weights=weights,
            fee=thegraph_data.swap_fee,
            type=thegraph_data.pool_type,
        )

    async def latest_block(self) -> BlockId:
        block = await self.client.get_last_block()
        return BlockId(number=block.number, hash=str(block.hash))

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:
        logger.debug(
            f'Retrieving balancer v2 state from TheGraph at block {block} ...'
        )

        extra_kwargs = block.to_thegraph_filter()

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
            'id_in': self.lp_ids,
            'pool_type_in': ['Weighted', 'LiquidityBootstrapping'],
            'swap_enabled': True,
            'is_paused': False
        }
        thegraph_data = [
            pool
            async for pool in self.client.get_pools_state(lp_filter, None, **extra_kwargs)
        ]
        state = {
            thegraph_lp_data.id: self.create_from_thegraph(thegraph_lp_data)
            for thegraph_lp_data in thegraph_data
        }

        #logger.debug(state)
        return state


class BalancerV2TheGraphAndWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries TheGraph for an initial state, and web3 for state updates."""

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        # Note: testing if we can use the same abi for all supported balancer pool types
        with open(Path(__file__).parent / 'artifacts' / 'WeightedPool.abi', 'r') as f:
            contract_abi = f.read()
        WeightedPool = web3_client.eth.contract(abi=contract_abi)

        lp_addresses = [lp_id[:42] for lp_id in lp_ids]
        self.lp_address_to_id = {
            lp_address: lp_id for lp_address, lp_id in zip(lp_addresses, lp_ids)
        }
        super().__init__(
            lp_addresses,
            [WeightedPool.events.Transfer],
            async_proxy,
            event_stream,
            web3_client
        )

    def get_state(self, prev_state: Dict[str, LP], changes: List[Any]) -> Dict[str, LP]:
        """Assembles state from previous state and updates."""

        cur_state = deepcopy(prev_state)

        for d in changes:
            lp_address = d.address.lower()
            lp_id = self.lp_address_to_id[lp_address]
            assert lp_id in cur_state.keys()
            lp_cur_state = cur_state[lp_id]

            assert d.event == "Transfer"
            print(d)
            is_mint = False
            try:
                from_token_index = lp_cur_state.tokens.index(d.args["from"])
            except ValueError:
                assert d.args["from"] == "0x0000000000000000000000000000000000000000"
                is_mint = True 

            is_burn = False
            try:
                to_token_index = lp_cur_state.tokens.index(d.args["to"])
            except ValueError:
                assert d.args["to"] == "0x0000000000000000000000000000000000000000"
                is_burn = True 

            if is_mint:
                lp_cur_state.balances[to_token_index] += d.args.value
            elif is_burn:
                lp_cur_state.balances[from_token_index] -= d.args.value
            else:
                lp_cur_state.balances[to_token_index] += d.args.value
                lp_cur_state.balances[from_token_index] -= d.args.value

            #print("updating state of ", lp_id, "from", prev_state[lp_id], "to", lp_cur_state, "@block", d.blockNumber)

        return cur_state


class BalancerV2Driver(LPDriver):
    def __init__(
        self,
        event_stream: EventStream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(BalancerV2)
        self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/balancer-labs/balancer-v2'
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.graphql_client = BalancerV2GraphQLClient(self.thegraph_url, session)

    def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        if data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        ]:
            async_proxy = BalancerV2TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
            return BalancerV2TheGraphAndWeb3Proxy(lp_ids, async_proxy, self.event_stream, self.web3_client)
        elif data_source == LPDriver.LPSyncProxyDataSource.TheGraph:
            async_proxy = BalancerV2TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        else:
            assert False # No other proxies are currently implemented for balancer.
        sync_proxy = LPSyncProxyFromAsyncProxy(
            async_proxy, self.block_stream
        )
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        def is_valid_pool(pool):
            return (
                float(pool.total_liquidity) >= 1000 and  # USD
                pool.pool_type in ['Weighted', 'LiquidityBootstrapping'] and 
                pool.swap_enabled and
                not pool.is_paused
            )

        ids = [
            pool.id
            for pool in await self.graphql_client.get_pools_containing_tokens(token_ids)
            if is_valid_pool(pool)
        ]
        return ids



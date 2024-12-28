import asyncio
import datetime
import logging
from copy import deepcopy
from dataclasses import dataclass
from decimal import Decimal as D
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy,
                    LPSyncProxy, LPSyncProxyFromAsyncProxy)
from lpbook.util import LP, ExchangeRate, Token, Trade
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream
from collections import defaultdict

from .subgraph import UniV3GraphQLClient
from dotenv import load_dotenv
import os

logger = logging.getLogger(__name__)

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")

@dataclass
class UniV3Like(LP):
    """UniswapV3 LP."""
    address: str
    token0: Token
    token1: Token
    sqrt_price: int
    liquidity: int
    tick: int
    liquidity_net: Dict[int, int]
    fee: int

    @property
    def uid(self) -> str:
        return self.address

    @classmethod
    @property
    def kind(self) -> str:
        return 'Concentrated'

    @property
    def tokens(self) -> List[Token]:
        return [self.token0, self.token1]

    @property
    def state(self) -> Dict:
        return {
            'sqrt_price': self.sqrt_price,
            'liquidity': self.liquidity,
            'tick': self.tick,
            'liquidity_net': self.liquidity_net,
            'fee': self.fee,
        }

    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/3270202 .
        return {
            'mean': 126908,
            'stddev': 32312,
        }

    @property
    def may_have_slippage(self) -> bool:
        return True

    @property
    def spot_xrates(self) -> dict[Tuple[Token, Token], ExchangeRate]:
        sqrt_price = self.sqrt_price / 2**96
        tb1 = 1
        tb2 = sqrt_price ** 2
        return {
            (self.tokens[0], self.tokens[1]): ExchangeRate(buy_token=self.tokens[0], sell_token=self.tokens[1], p_buy_over_p_sell=tb2/tb1),
            (self.tokens[1], self.tokens[0]): ExchangeRate(buy_token=self.tokens[1], sell_token=self.tokens[0], p_buy_over_p_sell=tb1/tb2),
        }


class UniV3(UniV3Like):
    """Uniswap V3 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Uniswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'


UniV3Like.as_univ3 = lambda self: UniV3(**self.__dict__)

class PancakeswapV3(UniV3Like):
    """Pancakeswap V3 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Pancakeswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'


UniV3Like.as_pancakeswapv3 = lambda self: PancakeswapV3(**self.__dict__)


class SolidlyV3(UniV3Like):
    """Solidly V3 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Solidly'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'


UniV3Like.as_solidlyv3 = lambda self: SolidlyV3(**self.__dict__)


class UniV3LikeTheGraphProxy(LPAsyncProxy):
    """Loads the state of liquidity from TheGraph."""
    def __init__(self, lp_ids, uniswap_v3_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = uniswap_v3_gql_client

    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[UniV3Like]:
        try:
            address = thegraph_data.id
            token0 = Token(
                address=thegraph_data.token0.id,
                symbol=thegraph_data.token0.symbol,
                decimals=int(thegraph_data.token0.decimals)
            )
            token1 = Token(
                address=thegraph_data.token1.id,
                symbol=thegraph_data.token1.symbol,
                decimals=int(thegraph_data.token1.decimals)
            )
            univ3 = UniV3Like(
                address=address,
                token0=token0,
                token1=token1,
                sqrt_price=int(thegraph_data.sqrt_price),
                liquidity=int(thegraph_data.liquidity),
                tick=int(thegraph_data.tick),
                liquidity_net={
                    int(tick.tick_idx): int(tick.liquidity_net)
                    for tick in thegraph_data.ticks
                },
                fee=D(thegraph_data.fee_tier)/D(1000000),
            )
        except TypeError:
            # Ignore ill-defined pools.
            return None

        return univ3 if len(univ3.liquidity_net) > 0 else None

    async def latest_block(self) -> BlockId:
        block = await self.client.get_last_block()
        return BlockId(number=block.number, hash=str(block.hash), timestamp=block.timestamp)

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:
        logger.debug(
            f'Retrieving uniswap V3 state from TheGraph at block {block} ...'
        )

        extra_kwargs = block.to_thegraph_filter()

        # this is to workaround a current thegraph bug (already reported and confirmed),
        # where thegraph replies with arbitrary data when the passed block number/hash is
        # not yet indexed.
        if block.number is not None:
            latest_block_number = (await self.latest_block()).number
            if block.number > latest_block_number:
                logger.debug(
                    f'{self} is lagging behind '
                    f'{block.number - latest_block_number} blocks.'
                )
                raise RuntimeError(f'Attempt to retrieve a block too recent for {self}')

        # Perform a more efficient query if we're tracking a single LP.
        if len(self.lp_ids) == 1:
            lp_id = list(self.lp_ids)[0]
            thegraph_lp_data = await self.client.get_pool_state_and_ticks(
                lp_id,
                **extra_kwargs
            )
            lp_state = self.create_from_thegraph(thegraph_lp_data, block=block)
            if lp_state is not None:
                state = {lp_id: lp_state}
        else:
            lp_filter = {'id_in': self.lp_ids}
            thegraph_data = await self.client.get_pools_state_and_ticks(
                lp_filter,
                {},
                **extra_kwargs
            )
            state = {}
            for thegraph_lp_data in thegraph_data:
                lp_state = self.create_from_thegraph(thegraph_lp_data, block=block)
                if lp_state is not None:
                    state[thegraph_lp_data.id] = lp_state

        if state.keys() != set(self.lp_ids):
            logger.error(f"Univ3 sync solver did not return all lp_ids: missing {set(self.lp_ids) - set(state.keys())}")
        return state


class UniV3TheGraphProxy(UniV3LikeTheGraphProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[UniV3]:
        univ3_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ3_like is None:
            return None
        return univ3_like.as_univ3()

class PancakeSwapV3TheGraphProxy(UniV3LikeTheGraphProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[PancakeswapV3]:
        univ3_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ3_like is None:
            return None
        return univ3_like.as_pancakeswapv3()


class SolidlyV3TheGraphProxy(UniV3LikeTheGraphProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[SolidlyV3]:
        univ3_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ3_like is None:
            return None
        return univ3_like.as_solidlyv3()


class UniV3LikeTheGraphAndWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries TheGraph for an initial state, and web3 for state updates."""

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client, abi_filename):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / abi_filename, 'r') as f:
            contract_abi = f.read()
        UniV3 = web3_client.eth.contract(abi=contract_abi)

        super().__init__(
            lp_ids,
            [UniV3.events.Swap, UniV3.events.Burn, UniV3.events.Mint],
            async_proxy,
            event_stream,
            web3_client
        )

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        lp_id = d.address.lower()
        if lp_id not in state.keys():
            return
        lp = state[lp_id]

        if d.event == 'Swap':
            lp.tick = d.args.tick
            lp.liquidity = d.args.liquidity
            lp.sqrt_price = d.args.sqrtPriceX96

        elif d.event == 'Mint':
            tick_lower = d.args.tickLower
            tick_upper = d.args.tickUpper

            assert d.args.amount is not None
            assert lp.liquidity is not None

            # liquidity tracks the liquidity on recent tick,
            # only need to update it if the new position includes the recent tick.
            if tick_lower <= lp.tick and lp.tick < tick_upper:
                lp.liquidity += d.args.amount

            if tick_lower not in lp.liquidity_net.keys():
                lp.liquidity_net[tick_lower] = 0

            if tick_upper not in lp.liquidity_net.keys():
                lp.liquidity_net[tick_upper] = 0

            lp.liquidity_net[tick_lower] += d.args.amount
            lp.liquidity_net[tick_upper] -= d.args.amount

            # remove 0 entries to save bandwidth
            if lp.liquidity_net[tick_lower] == 0:
                lp.liquidity_net.pop(tick_lower)
            if lp.liquidity_net[tick_upper] == 0:
                lp.liquidity_net.pop(tick_upper)

        elif d.event == 'Burn':
            tick_lower = d.args.tickLower
            tick_upper = d.args.tickUpper

            assert d.args.amount is not None
            assert lp.liquidity is not None

            # liquidity tracks the liquidity on recent tick,
            # only need to update it if the new position includes the recent tick.
            if tick_lower <= lp.tick and lp.tick < tick_upper:
                lp.liquidity -= d.args.amount

            if tick_lower not in lp.liquidity_net.keys():
                lp.liquidity_net[tick_lower] = 0

            if tick_upper not in lp.liquidity_net.keys():
                lp.liquidity_net[tick_upper] = 0

            lp.liquidity_net[tick_lower] -= d.args.amount
            lp.liquidity_net[tick_upper] += d.args.amount

            # remove 0 entries to save bandwidth
            if lp.liquidity_net[tick_lower] == 0:
                lp.liquidity_net.pop(tick_lower)
            if lp.liquidity_net[tick_upper] == 0:
                lp.liquidity_net.pop(tick_upper)

        else:
            assert False


    def get_trades(self, cur_state: Dict[str, LP], changes: List[Any]) -> list[Trade]:
        """Assembles list of trades from updates."""
        trades = []
        for d in changes:
            if d.event != 'Swap':
                continue
            lp_id = d.address.lower()
            if lp_id not in cur_state.keys():
                continue
            lp_cur_state = cur_state[lp_id]
            trade = Trade(
                lp_id=lp_id,
                block_number=d.blockNumber,
                token1=lp_cur_state.token0,
                token2=lp_cur_state.token1,
                buy_amount1=d.args.amount0,
                buy_amount2=d.args.amount1,
            )
            trades.append(trade)

        return trades

class UniV3LikeDriver(LPDriver):
    def __init__(
        self,
        event_stream: EventStream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client
    ):
        super().__init__(self.UniV3Like)
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.graphql_client = UniV3GraphQLClient(self.thegraph_url, session)

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        async_proxy = self.UniV3LikeTheGraphProxy(lp_ids, self.graphql_client)
        if data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        ]:
            sync_proxy = self.UniV3LikeTheGraphAndWeb3Proxy(
                lp_ids,
                async_proxy,
                self.event_stream,
                self.web3_client,
                self.abi_filename
            )
        elif data_source == LPDriver.LPSyncProxyDataSource.TheGraph:
            sync_proxy = LPSyncProxyFromAsyncProxy(async_proxy, self.block_stream)
        else:
            assert False
        return sync_proxy

    def create_lp_async_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPAsyncProxyDataSource =
            LPDriver.LPAsyncProxyDataSource.Default
    ) -> LPAsyncProxy:
        if data_source in [
            LPDriver.LPAsyncProxyDataSource.Default,
            LPDriver.LPAsyncProxyDataSource.TheGraph
        ]:
            return self.UniV3LikeTheGraphProxy(
                lp_ids, self.graphql_client
            )

        raise RuntimeError("Invalid data_source for async_proxy to UniV3")

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        return [
            state.id async for state in self.graphql_client.get_pools_state(
                {
                    'token0_in': token_ids,
                    'token1_in': token_ids,
                    'liquidity_gt': 0,
                    'total_value_locked_usd_gt': 1000
                },
                field_setter=self.graphql_client.set_pool_id_field
            )
        ]

class UniV3Driver(UniV3LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV'
        self.UniV3Like = UniV3
        self.UniV3LikeTheGraphProxy = UniV3TheGraphProxy
        self.UniV3LikeTheGraphAndWeb3Proxy = UniV3LikeTheGraphAndWeb3Proxy
        self.abi_filename = 'uniswap_v3.abi'
        super().__init__(*args, **kwargs)


class PancakeswapV3Driver(UniV3LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/pancakeswap/exchange-v3-eth'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/CJYGNhb7RvnhfBDjqpRnD3oxgyhibzc7fkAMa38YV3oS'
        self.UniV3Like = PancakeswapV3
        self.UniV3LikeTheGraphProxy = PancakeSwapV3TheGraphProxy
        self.UniV3LikeTheGraphAndWeb3Proxy = UniV3LikeTheGraphAndWeb3Proxy
        self.abi_filename = 'pancakeswap_v3.abi'
        super().__init__(*args, **kwargs)


class SolidlyV3Driver(UniV3LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/pancakeswap/exchange-v3-eth'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/7StqFFqbxi3jcN5C9YxhRiTxQM8HA8XEHopsynqqxw3t'
        self.UniV3Like = SolidlyV3
        self.UniV3LikeTheGraphProxy = SolidlyV3TheGraphProxy
        self.UniV3LikeTheGraphAndWeb3Proxy = UniV3LikeTheGraphAndWeb3Proxy
        self.abi_filename = 'solidly_v3.abi'
        super().__init__(*args, **kwargs)


import asyncio
from itertools import permutations
import logging
from copy import deepcopy
from dataclasses import dataclass
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from async_lru import alru_cache
from math import ceil, sqrt
from pathlib import Path
from typing import Any, Dict, List, Tuple

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy,
                    LPSyncProxy, LPSyncProxyFromAsyncProxy, MultiLPFromInitialStatePlusChangesProxy)
from lpbook.error import TemporaryError
from lpbook.lps.uniswap_v2.subgraph import UniV2GraphQLClient
from lpbook.thegraph.subgraph import GraphQLClientError
from lpbook.util import LP, ExchangeRate, Token, Trade
from lpbook.web3 import BlockId, create_token_from_web3, get_erc20_contract
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream
from web3.exceptions import BlockNotFound, ContractLogicError
from dotenv import load_dotenv
import os

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))

logger = logging.getLogger(__name__)

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

@dataclass
class UniV2Like(LP):
    """Uniswap V2 / Sushiswap / Pancakeswap V2 LP."""
    address: str
    _tokens: List[Token]
    balances: List[int]
    lp_token_balance: int

    @classmethod
    @property
    def kind(self) -> str:
        return 'ConstProd'

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def uid(self) -> str:
        return self.address

    @property
    def state(self) -> Dict:
        return {
            'balances': self.balances,
            'lp_token_balance': self.lp_token_balance
        }

    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/1043253 .
        return {
            'nr_obs': 39409,
            'mean': 100000,
            'stddev': 0,
            'min': 30132,
            'max': 695127,
            'median': 97511
        }

    @property
    def spot_xrates(self) -> dict[Tuple[Token, Token], ExchangeRate]:
        r = {}
        for i, j in permutations(range(len(self.tokens)), 2):
            t_b = self.tokens[i]
            t_s = self.tokens[j]
            r_b = self.balances[i] 
            r_s =self.balances[j]
            r[t_b, t_s] = ExchangeRate(
                buy_token=t_b,
                sell_token=t_s,
                p_buy_over_p_sell=r_s / r_b
            )
        return r

class UniV2(UniV2Like):
    """Uniswap V2 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Uniswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'


UniV2Like.as_univ2 = lambda self: UniV2(**self.__dict__)


class Sushi(UniV2Like):
    """Sushiswap LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Sushiswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'


UniV2Like.as_sushi = lambda self: Sushi(**self.__dict__)

class PancakeswapV2(UniV2Like):
    """Pancakeswap LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Pancakeswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'


UniV2Like.as_pancakeswapv2 = lambda self: PancakeswapV2(**self.__dict__)


class SwaprV2(UniV2Like):
    """SwaprV2 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Swapr'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '2'


UniV2Like.as_swaprv2 = lambda self: SwaprV2(**self.__dict__)


class UniV2LikeWeb3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the uniswap v2 LP through web3."""

    def __init__(self, lp_ids, web3_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.web3_client = web3_client
        self.contracts = {}

        with open(Path(__file__).parent / 'artifacts' / 'uniswap_v2.abi', 'r') as f:
            contract_abi = f.read()
            for lp_id in lp_ids:
                lp_id_chksum = self.web3_client.to_checksum_address(lp_id)
                self.contracts[lp_id] = web3_client.eth.contract(
                    address=lp_id_chksum,
                    abi=contract_abi
                )

    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block()
        return BlockId.from_web3(block)

    @alru_cache
    async def get_tokens(self, lp_id) -> Tuple[Token, Token]:
        token0_address = await (self.contracts[lp_id].functions.token0().call()).lower()
        token1_address = await (self.contracts[lp_id].functions.token1().call()).lower()

        token0_address = self.web3_client.to_checksum_address(token0_address)
        token1_address = self.web3_client.to_checksum_address(token1_address)

        return asyncio.gather(
            create_token_from_web3(token0_address, self.web3_client),
            create_token_from_web3(token1_address, self.web3_client)
        )
        

    async def create_from_blockchain(self, lp_id, block: BlockId) -> UniV2Like:
        block_identifier = block.to_web3()

        token0, token1 = await self.get_tokens(lp_id)
        balance0, balance1, _ = await self.contracts[lp_id].functions.getReserves().call(
            block_identifier=block_identifier
        )
        total_supply = await self.contracts[lp_id].functions.totalSupply().call(
            block_identifier=block_identifier
        )

        return UniV2Like(
            address=lp_id,
            _tokens=[token0, token1],
            balances=[balance0, balance1],
            lp_token_balance=total_supply
        )

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        logger.debug(
            f'Retrieving uni v2 like state from blockchain at block {block} ...'
        )

        state = {}

        async def add_to_state(lp_id):
            try:
                state[lp_id] = await self.create_from_blockchain(
                    lp_id,
                    block
                )
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

        # logger.debug(state)
        return state


class UniV2Web3AsyncProxy(UniV2LikeWeb3AsyncProxy):
    async def create_from_blockchain(self, lp_id, block: BlockId) -> UniV2:
        return await (super().create_from_blockchain(lp_id, block)).as_univ2()


class SushiWeb3AsyncProxy(UniV2LikeWeb3AsyncProxy):
    async def create_from_blockchain(self, lp_id, block: BlockId) -> UniV2:
        return await (super().create_from_blockchain(lp_id, block)).as_sushi()

class PancakeswapV2Web3AsyncProxy(UniV2LikeWeb3AsyncProxy):
    async def create_from_blockchain(self, lp_id, block: BlockId) -> UniV2:
        return await (super().create_from_blockchain(lp_id, block)).as_pancakeswapv2()

class SwaprV2Web3AsyncProxy(UniV2LikeWeb3AsyncProxy):
    async def create_from_blockchain(self, lp_id, block: BlockId) -> UniV2:
        return await (super().create_from_blockchain(lp_id, block)).swaprv2()

class UniV2LikeTheGraphAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the uniswap v2 LP through TheGraph."""
    def __init__(self, lp_ids, uniswap_v2_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = uniswap_v2_gql_client

    def create_from_thegraph(self, thegraph_data, block: BlockId) -> UniV2Like:
        tokens = [
            Token(
                address=thegraph_data.token0.id,
                symbol=thegraph_data.token0.symbol,
                decimals=int(thegraph_data.token0.decimals)
            ),
            Token(
                address=thegraph_data.token1.id,
                symbol=thegraph_data.token1.symbol,
                decimals=int(thegraph_data.token1.decimals)
            )
        ]
        balances = [
            int(D(thegraph_data.reserve0) * 10**int(tokens[0].decimals)),
            int(D(thegraph_data.reserve1) * 10**int(tokens[1].decimals))
        ]
        lp_token_balance = int(D(thegraph_data.total_supply) * 10**18)

        return UniV2Like(
            address=thegraph_data.id,
            _tokens=tokens,
            balances=balances,
            lp_token_balance=lp_token_balance
        )

    async def latest_block(self) -> BlockId:
        block = await self.client.get_last_block()
        return BlockId.from_web3(block)

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:
        logger.debug(
            f'Retrieving uniswap v2 like state from TheGraph at block {block} ...'
        )

        extra_kwargs = block.to_thegraph_filter()

        # this is to workaround a current thegraph bug (already reported and confirmed),
        # where thegraph replies with arbitrary data when the passed block number/hash is
        # not yet indexed.
        if block.number is not None:
            while True:
                latest_block_number = (await self.latest_block()).number
                if block.number <= latest_block_number:
                    break
                logger.debug(
                    f'{self} is lagging behind '
                    f'{block.number - latest_block_number} blocks from block {block.number}. Retrying ...'
                )
                await asyncio.sleep(2)

        lp_filter = {
            'id_in': self.lp_ids,
        }
        while True:
            try:
                thegraph_data = [
                    pair
                    async for pair in self.client.get_pairs_state(lp_filter, None, **extra_kwargs)
                ]
                break
            except GraphQLClientError as e:
                logger.debug(
                    f'{self} is not able to fetch data from thegraph. Retrying ...'
                )
                await asyncio.sleep(2)  # wait a bit to allow thegraph to catchup

        state = {
            thegraph_lp_data.id: self.create_from_thegraph(thegraph_lp_data, block=block)
            for thegraph_lp_data in thegraph_data
        }

        # logger.debug(state)
        return state


class UniV2TheGraphAsyncProxy(UniV2LikeTheGraphAsyncProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> UniV2:
        univ2_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ2_like is None:
            return univ2_like
        return univ2_like.as_univ2()


class SushiTheGraphAsyncProxy(UniV2LikeTheGraphAsyncProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Sushi:
        univ2_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ2_like is None:
            return univ2_like
        return univ2_like.as_sushi()

class PancakeswapV2TheGraphAsyncProxy(UniV2LikeTheGraphAsyncProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> PancakeswapV2:
        univ2_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ2_like is None:
            return univ2_like
        return univ2_like.as_pancakeswapv2()

class SwaprV2TheGraphAsyncProxy(UniV2LikeTheGraphAsyncProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> SwaprV2:
        univ2_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ2_like is None:
            return univ2_like
        return univ2_like.as_swaprv2()

class UniV2LikeTheGraphAndWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries TheGraph for an initial state, and web3 for state updates."""

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / 'uniswap_v2.abi', 'r') as f:
            contract_abi = f.read()
        UniV2 = web3_client.eth.contract(abi=contract_abi)

        super().__init__(
            lp_ids,
            [UniV2.events.Sync],
            async_proxy,
            event_stream,
            web3_client
        )

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""
        lp_id = d.address.lower()
        if lp_id not in state.keys():
            return
        lp = state[lp_id]

        assert d.event == 'Sync'
        lp.balances[0] = d.args.reserve0
        lp.balances[1] = d.args.reserve1


    def get_trades(self, prev_state: Dict[str, LP], changes: List[Any]) -> list[Trade]:
        """Assembles list of trades from updates."""
        trades = []

        cur_state = deepcopy(prev_state)

        for d in changes:
            lp_id = d.address.lower()
            if lp_id not in cur_state.keys():
                continue
            lp_cur_state = cur_state[lp_id]

            #if d.event != 'Swap':
            #    continue
            assert d.event == 'Sync'
            buy_amount1 = d.args.reserve0 - lp_cur_state.balances[0]
            buy_amount2 = d.args.reserve1 - lp_cur_state.balances[1]
            # this is not a mistake! Since we need to diff to the reserves to obtain the deltas, 
            # we need to update the reserves since several d in changes can refer to the same lp_id 
            lp_cur_state.balances[0] = d.args.reserve0  
            lp_cur_state.balances[1] = d.args.reserve1

            trade = Trade(
                lp_id=lp_id,
                block_number=d.blockNumber,
                token1=lp_cur_state.tokens[0],
                token2=lp_cur_state.tokens[1],
                buy_amount1=buy_amount1, # d.args.amount0In-d.args.amount0Out,
                buy_amount2=buy_amount2, # d.args.amount1In-d.args.amount1Out,
            )
            trades.append(trade)

        return trades


class UniV2LikeLPTheGraphAndWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries Web3 for an initial state and for state updates."""

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        ERC20 = get_erc20_contract(None, web3_client)
        super().__init__(
            lp_ids,
            [ERC20.events.Transfer],
            async_proxy,
            event_stream,
            web3_client
        )

    def get_state(self, prev_state: Dict[str, LP], changes: List[Any]) -> Dict[str, LP]:
        """Assembles state from previous state and updates."""

        cur_state = deepcopy(prev_state)

        print("HERE", changes)
        for d in changes:
            assert d.event == 'Transfer'

            from_ = d.args["from"].lower()
            to = d.args.to.lower()
            value = int(d.args.value)

            print("HERE", d)

            # mint
            if from_ == ZERO_ADDRESS and to in cur_state.keys():
                lp_id = to
                cur_state[lp_id].lp_token_balance += value
            # burn
            elif from_ in cur_state.keys() and to == ZERO_ADDRESS:
                lp_id = from_
                cur_state[lp_id].lp_token_balance -= value
            
        return cur_state

class UniV2LikeDriver(LPDriver):
    def __init__(
        self,
        event_stream: EventStream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(self.UniV2Like)
        self.event_stream = event_stream
        self.block_stream = block_stream
        self.web3_client = web3_client
        self.graphql_client = UniV2GraphQLClient(self.thegraph_url, session)

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        if data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        ]:
            async_proxy = self.UniV2LikeTheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
            sync_proxy_1 = UniV2LikeTheGraphAndWeb3Proxy(
                lp_ids,
                async_proxy,
                self.event_stream,
                self.web3_client
            )
            #sync_proxy_2 = UniV2LikeLPTheGraphAndWeb3Proxy(
            #    lp_ids,
            #    async_proxy,
            #    self.event_stream,
            #    self.web3_client
            #)
            #sync_proxy = MultiLPFromInitialStatePlusChangesProxy([sync_proxy_1, sync_proxy_2])
            sync_proxy = sync_proxy_1
            return sync_proxy
        elif data_source == LPDriver.LPSyncProxyDataSource.Web3:
            async_proxy = self.UniV2LikeWeb3AsyncProxy(lp_ids, self.web3_client)
        else:
            assert data_source == LPDriver.LPSyncProxyDataSource.TheGraph
            async_proxy = self.UniV2LikeTheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        sync_proxy = LPSyncProxyFromAsyncProxy(
            async_proxy, self.block_stream
        )
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
            return self.UniV2LikeTheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        elif data_source == LPDriver.LPAsyncProxyDataSource.Web3:
            return self.UniV2LikeWeb3AsyncProxy(lp_ids, self.web3_client)

        raise RuntimeError("Invalid data_source for async_proxy to UniV2 like")

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        def is_valid_token(token):
            return token.symbol is not None and len(token.symbol) > 0 and \
                token.decimals is not None

        return [
            state.id
            async for state in self.graphql_client.get_pairs_state(
                {
                    'token0_in': token_ids,
                    'token1_in': token_ids,
                    'reserve_usd_gt': 1000
                },
                field_setter=self.graphql_client.set_pair_id_and_tokens_fields
            )
            if is_valid_token(state.token0) and is_valid_token(state.token1)
        ]


class UniV2Driver(UniV2LikeDriver):
    def __init__(self, *args, **kwargs):
        # The official hosted subgraph seems to be stuck (and incorrect!):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
        # This is an alternative:
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v2-dev'
        # This is the official GRT network instance
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/A3Np3RQbaBA6oKJgiwDJeo5T3zrYfGHPWFYayMwtNDum'
        self.UniV2Like = UniV2
        self.UniV2LikeWeb3AsyncProxy = UniV2Web3AsyncProxy
        self.UniV2LikeTheGraphAsyncProxy = UniV2TheGraphAsyncProxy
        super().__init__(*args, **kwargs)


class SushiDriver(UniV2LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/sushiswap/exchange'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/6NUtT5mGjZ1tSshKLf5Q3uEEJtjBZJo1TpL5MXsUBqrT'
        self.UniV2Like = Sushi
        self.UniV2LikeWeb3AsyncProxy = SushiWeb3AsyncProxy
        self.UniV2LikeTheGraphAsyncProxy = SushiTheGraphAsyncProxy
        super().__init__(*args, **kwargs)


class PancakeswapV2Driver(UniV2LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/pancakeswap/exhange-eth'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/9opY17WnEPD4REcC43yHycQthSeUMQE26wyoeMjZTLEx'
        self.UniV2Like = PancakeswapV2
        self.UniV2LikeWeb3AsyncProxy = PancakeswapV2Web3AsyncProxy
        self.UniV2LikeTheGraphAsyncProxy = PancakeswapV2TheGraphAsyncProxy
        super().__init__(*args, **kwargs)

class SwaprV2Driver(UniV2LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/pancakeswap/exhange-eth'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/CfBvQzwWyg41ceiR3XM64KzJiAKVPML4iztwEaHYdCFw'
        self.UniV2Like = SwaprV2
        self.UniV2LikeWeb3AsyncProxy = SwaprV2Web3AsyncProxy
        self.UniV2LikeTheGraphAsyncProxy = SwaprV2TheGraphAsyncProxy
        super().__init__(*args, **kwargs)



import asyncio
from copy import deepcopy
from functools import cache
from itertools import permutations
import logging
from dataclasses import dataclass
from fractions import Fraction as F
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import aiohttp
from lpbook import (LPAsyncProxy, LPDriver, LPFromInitialStatePlusChangesProxy,
                    LPSyncProxy, LPSyncProxyFromAsyncProxy, MultiLPFromInitialStatePlusChangesProxy)
from lpbook.lps.balancer_v2.common import BalancerV2BalancesWeb3SyncProxy, BalancerV2FeesWeb3SyncProxy
from lpbook.lps.balancer_v2.subgraph import BalancerV2GraphQLClient
from lpbook.util import LP, ExchangeRate, Token, Trade
from lpbook.web3 import BlockId, TokenDB
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import EventStream
from lpbook.error import TemporaryError
from web3.exceptions import BlockNotFound, ContractLogicError

from dotenv import load_dotenv
import os

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))

logger = logging.getLogger(__name__)

def lp_id_to_address(lp_id) -> str:
    return lp_id[:42]


# Currently only supports Weighted type.

@dataclass
class BalancerV2(LP):
    """Balancer V2."""
    _id: str
    all_tokens: List[Token]
    balances: List[int]
    weights: List[str]
    fee_e18: int
    type: str
    owner: str

    @property
    def tokens(self) -> List[Token]:
        return self.all_tokens

    @property
    def uid(self) -> str:
        return self._id

    @property
    def fee_discount_factor(self) -> Optional[F]:
        if self.owner != "0xba1ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1b":
            return None
        # Applying 80% discount in bounty
        return F(20, 100)

    @property
    def state(self) -> Dict:
        fee = F(self.fee_e18, int(1e18))
        if self.fee_discount_factor is not None:
            fee = fee * self.fee_discount_factor
        return {
            'type': self.type,
            'balances': self.balances,
            'weights': self.weights,
            'fee': fee, 
        }

    @property
    def execution_info(self):
        if self.fee_discount_factor is None:
            return {}
        return {
            'fee_discount_factor': self.fee_discount_factor     # to issue the required set/unset fee contract calls
        }
    
    @classmethod
    @property
    def kind(self) -> str:
        return 'WeightedProd'

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
        return {
            'mean': 88892, 
            'stddev': 0
        }

    @property
    def address(self) -> str:
        return lp_id_to_address(self._id)

    @property
    def may_have_slippage(self) -> bool:
        return True

    @property
    def spot_xrates(self) -> dict[Tuple[Token, Token], ExchangeRate]:
        r = {}
        for i, j in permutations(range(len(self.tokens)), 2):
            t_b = self.tokens[i]
            t_s = self.tokens[j]
            w_b = float(self.weights[i])
            w_s = float(self.weights[j])
            r_b = self.balances[i] 
            r_s =self.balances[j]
            r[t_b, t_s] = ExchangeRate(
                buy_token=t_b,
                sell_token=t_s,
                p_buy_over_p_sell=r_s * w_b / (r_b * w_s)
            )
        return r
        
class BalancerV2TheGraphAsyncProxy(LPAsyncProxy):
    """"Proxies the state of the balancer v2 LP through TheGraph."""
    def __init__(self, lp_ids, balancer_v2_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = balancer_v2_gql_client

    def create_from_thegraph(self, thegraph_data, block: BlockId) -> BalancerV2:
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
        lp_id = thegraph_data.id

        return BalancerV2(
            _id=lp_id,
            all_tokens=tokens,
            balances=balances,
            weights=weights,
            fee_e18=thegraph_data.swap_fee * 1e18,
            type=thegraph_data.pool_type,
            owner=thegraph_data.owner.lower()
        )

    async def latest_block(self) -> BlockId:
        block = await self.client.get_last_block()
        return BlockId(number=block.number, hash=str(block.hash), timestamp=block.timestamp)

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
            'pool_type_in': ['Weighted'],
            'swap_enabled': True,
            'is_paused': False
        }
        thegraph_data = [
            pool
            async for pool in self.client.get_pools_state(lp_filter, None, **extra_kwargs)
        ]
        state = {
            thegraph_lp_data.id: self.create_from_thegraph(thegraph_lp_data, block=block)
            for thegraph_lp_data in thegraph_data
        }

        #logger.debug(state)
        return state

class BalancerV2Web3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the balancer v2 LP through web3."""
    vault_address = "0xba12222222228d8ba445958a75a0704d566bf2c8"
    def __init__(self, lp_ids, web3_client, token_db: TokenDB):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = web3_client
        self.token_db = token_db

        with open(Path(__file__).parent / 'artifacts' / 'Vault.abi', 'r') as f:
            vault_abi = f.read()
            vault_address_chksum = self.client.to_checksum_address(self.vault_address)
            self.Vault = web3_client.eth.contract(
                address=vault_address_chksum,
                abi=vault_abi
                )

        self.WeightedPool = {} 
        with open(Path(__file__).parent / 'artifacts' / 'WeightedPool.abi', 'r') as f:
            weighted_pool_abi = f.read()
            for lp_id in lp_ids:
                address = lp_id_to_address(lp_id)
                address_chksum = self.client.to_checksum_address(address)
                self.WeightedPool[lp_id] = web3_client.eth.contract(
                    address=address_chksum,
                    abi=weighted_pool_abi
                )

    async def latest_block(self) -> BlockId:
        block = self.client.eth.get_block("latest")
        return BlockId(number=block.number, hash=block.hash.hex())

    async def create_from_blockchain(self, lp_id, block: BlockId) -> Optional[BalancerV2]:
        block_identifier = block.to_web3()

        def f():
            tokens, balances, _ = self.Vault.functions.getPoolTokens(lp_id).call(
                block_identifier=block_identifier
            )
            weights = self.WeightedPool[lp_id].functions.getNormalizedWeights().call(
                block_identifier=block_identifier
            )
            weights = [str(w * 1e-18) for w in weights]

            fee_e18 = self.WeightedPool[lp_id].functions.getSwapFeePercentage().call(
                block_identifier=block_identifier
            )
            owner = self.WeightedPool[lp_id].functions.getOwner().call(
                block_identifier=block_identifier
            ).lower()
            return (tokens, balances, weights, fee_e18, owner)

        tokens, balances, weights, fee_e18, owner = await asyncio.to_thread(f)

        tokens = [await self.token_db.get(token) for token in tokens]

        if any(token is None for token in tokens):
            return None
        
        balances = [int(balance) for balance in balances]

        return BalancerV2(
            _id=lp_id,
            all_tokens=tokens,
            balances=balances,
            weights=weights,
            fee_e18=fee_e18,        
            type="Weighted",
            owner=owner
        )

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        logger.debug(
            f'Retrieving balancer v2 like state from blockchain at block {block} ...'
        )

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

class BalancerV2Driver(LPDriver):
    def __init__(
        self,
        token_db: TokenDB,
        event_stream: EventStream,
        block_stream: BlockStream,
        session: aiohttp.ClientSession,
        web3_client=None
    ):
        super().__init__(BalancerV2)
        self.token_db = token_db
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/balancer-labs/balancer-v2'
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
        if data_source in [
            #LPDriver.LPSyncProxyDataSource.Default,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        ]:
            async_proxy = BalancerV2TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        elif data_source in [
            LPDriver.LPSyncProxyDataSource.Default,
            #LPDriver.LPSyncProxyDataSource.Web3
        ]:
            async_proxy = BalancerV2Web3AsyncProxy(
                lp_ids, self.web3_client, self.token_db
            )
        elif data_source == LPDriver.LPSyncProxyDataSource.TheGraph:
            async_proxy = BalancerV2TheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
            sync_proxy = LPSyncProxyFromAsyncProxy(
                async_proxy, self.block_stream
            )
            return sync_proxy
        else:
            assert False # No other proxies are currently implemented for balancer.
        
        sync_proxy_1 = BalancerV2BalancesWeb3SyncProxy(lp_ids, async_proxy, self.event_stream, self.web3_client)
        sync_proxy_2 = BalancerV2FeesWeb3SyncProxy(lp_ids, async_proxy, self.event_stream, self.web3_client) 
        return MultiLPFromInitialStatePlusChangesProxy([sync_proxy_1, sync_proxy_2])

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        def is_valid_pool(pool):
            return (
                float(pool.total_liquidity) >= 1000 and  # USD
                pool.pool_type == 'Weighted' and 
                pool.swap_enabled and
                not pool.is_paused
            )

        ids = [
            pool.id
            for pool in await self.graphql_client.get_pools_containing_tokens(token_ids)
            if is_valid_pool(pool)
        ]
        return ids



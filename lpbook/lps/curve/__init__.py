
import asyncio
from enum import Enum
import logging
from copy import deepcopy
from dataclasses import dataclass
from decimal import MAX_EMAX, MAX_PREC, MIN_EMIN, Context
from decimal import Decimal as D
from decimal import setcontext
from functools import cache
from pathlib import Path
from typing import Dict, List, Tuple

import aiohttp
from lpbook.lps.curve.subgraph import CurveGraphQLClient
from lpbook import (CacheMissError, LPSyncProxyFromAsyncProxy,
                          LPSyncProxy, LPDriver, LPAsyncProxy, RecentStateCache)
from lpbook.util import LP, Token
from lpbook.web3 import create_token_from_web3, Block
from lpbook.web3.BlockIndex import BlockIndex
from web3.constants import ADDRESS_ZERO

setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))

logger = logging.getLogger(__name__)


@dataclass
class Curve(LP):
    """Represents a Curve LP."""
    address: str
    _tokens: List[Token]
    amplification_parameter: int
    balances: List[int]
    fee: int

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def uid(self) -> str:
        return self.address

    @property
    def type(self) -> str:
        return 'Curve'

    @property
    def state(self) -> Dict:
        return {
            "amplification_parameter": self.amplification_parameter,
            "fee": self.fee,
        }


class CurveWeb3AsyncProxy(LPAsyncProxy):
    REGISTRY_CONTRACT_ADDRESS = '0x90e00ace148ca3b23ac1bc8c240c2a7dd9c2d7f5'

    def __init__(self, lp_ids, web3_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = web3_client

        with open(Path(__file__).parent / "artifacts" / "registry.abi", "r") as f:
            registry_contract_abi = f.read()
            registry_chksum = web3_client.toChecksumAddress(
                self.REGISTRY_CONTRACT_ADDRESS
            )
            self.registry_contract = web3_client.eth.contract(
                address=registry_chksum,
                abi=registry_contract_abi
            )

    async def latest_block(self) -> Block:
        block = await self.client.eth.get_block()
        return Block(number=block.number, hash=str(block.hash))

    @cache
    def get_tokens(self, lp_id_chksum) -> List[Token]:
        coins = self.registry_contract.functions.get_coins(lp_id_chksum).call()
        tokens = []
        i = 0
        while coins[i] != ADDRESS_ZERO:
            tokens.append(create_token_from_web3(coins[i], self.client))
            i += 1
        return tokens

    def get_block_identifier(self, block_number, block_hash):
        if block_hash is not None:
            return block_hash
        elif block_number is not None:
            return block_number
        else:
            return 'latest'

    def create_from_blockchain(self, lp_id, block_number=None, block_hash=None) -> Curve:
        block_identifier = self.get_block_identifier(block_number, block_hash)
        lp_id_chksum = self.client.toChecksumAddress(lp_id)

        balances = self.registry_contract.functions.get_balances(lp_id_chksum).call(
            block_identifier=block_identifier
        )
        tokens = self.get_tokens(lp_id_chksum)
        nr_tokens = len(tokens)
        balances = balances[:nr_tokens]

        parameters = self.registry_contract.functions.get_parameters(lp_id_chksum).call(
            block_identifier=block_identifier
        )
        PARAMETER_A_IDX = 0
        PARAMETER_FEE_IDX = 2
        return Curve(
            address=lp_id,
            _tokens=tokens,
            amplification_parameter=parameters[PARAMETER_A_IDX],
            balances=balances,
            fee=D(parameters[PARAMETER_FEE_IDX])/D(1e10),
        )

    async def __call__(self, block_number: int = None, block_hash: str = None) -> Dict[str, LP]:
        short_block_hash = block_hash[:8] if block_hash is not None else None
        logger.debug(f"Retrieving curve state from blockchain at block {block_number}/{short_block_hash} ...")

        state = {}

        async def add_to_state(lp_id):
            state[lp_id] = await asyncio.to_thread(
                self.create_from_blockchain,
                lp_id,
                block_number,
                block_hash
            )

        await asyncio.gather(
            *[add_to_state(lp_id) for lp_id in self.lp_ids]
        )

        # logger.debug(state)
        return state


class CurveTheGraphAsyncProxy(LPAsyncProxy):
    """"Loads the state of liquidity from TheGraph."""
    def __init__(self, lp_ids, curve_gql_client):
        assert len(lp_ids) >= 1
        self.lp_ids = lp_ids
        self.client = curve_gql_client

    def create_from_thegraph(self, thegraph_data) -> Curve:
        tokens = [None] * len(thegraph_data.coins)
        balances = [None] * len(thegraph_data.coins)
        for coin in thegraph_data.coins:
            tokens[coin.index] = Token(
                address=coin.token.id,
                symbol=coin.token.symbol,
                decimals=int(coin.token.decimals)
            )
            balances[coin.index] = int(D(coin.balance) * 10**int(coin.token.decimals))

        return Curve(
            address=thegraph_data.id,
            _tokens=tokens,
            amplification_parameter=int(thegraph_data.a),
            balances=balances,
            fee=D(thegraph_data.fee),
        )

    async def latest_block(self) -> Block:
        block = await self.client.get_last_block()
        return Block(number=block.number, hash=str(block.hash))

    async def __call__(
        self,
        block_number: int = None,
        block_hash: str = None
    ) -> Dict[str, LP]:
        shortened_block_hash = block_hash[:8] if block_hash is not None else None
        logger.debug(
            "Retrieving curve state from TheGraph at block "
            f"{block_number}/{shortened_block_hash} ..."
        )

        block = {}
        if block_hash is not None:
            block.update(hash=block_hash)
        elif block_number is not None:
            block.update(number=block_number)

        extra_kwargs = {}
        if len(block) > 0:
            extra_kwargs = {"block": block}

        # this is to workaround a current thegraph bug (already reported and confirmed),
        # where thegraph replies with arbitrary data when the passed block number/hash is
        # not yet indexed.
        if block_number is not None:
            latest_block_number = (await self.latest_block()).number
            if block_number > latest_block_number:
                logger.debug(f"{self} is lagging behind {block_number - latest_block_number} blocks.")
                raise RuntimeError(f"Attempt to retrieve a block too recent for {self}")

        lp_filter = {'id_in': self.lp_ids}
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


class CurveDriver(LPDriver):
    class Proxy(Enum):
        TheGraph = 1
        Web3 = 2

    def __init__(
        self,
        block_index: BlockIndex,
        session: aiohttp.ClientSession,
        web3_client=None,
        proxy: Proxy = Proxy.TheGraph
    ):
        self.block_index = block_index
        if proxy == CurveDriver.Proxy.Web3:
            assert web3_client is not None
            self.web3_client = web3_client
        self.graphql_client = CurveGraphQLClient(session)
        self.proxy = proxy

    def type(self) -> str:
        return "Curve"

    def create_lp_sync_proxy(self, lp_ids: List[str]) -> LPSyncProxy:
        if self.proxy == CurveDriver.Proxy.Web3:
            async_proxy = CurveWeb3AsyncProxy(lp_ids, self.web3_client)
        else:
            async_proxy = CurveTheGraphAsyncProxy(
                lp_ids, self.graphql_client
            )
        sync_proxy = LPSyncProxyFromAsyncProxy(
            async_proxy, self.block_index
        )
        return sync_proxy

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        return {
            lp.id
            async for lp in self.graphql_client.get_pools_state({'isMeta': False})
            if len({coin.token.id for coin in lp.coins} & set(token_ids)) >= 2
        }
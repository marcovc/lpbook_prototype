

import asyncio
from dataclasses import dataclass
from datetime import time
import logging
import math
import os
from pathlib import Path
from typing import Dict, List
from async_lru import alru_cache
from web3 import AsyncWeb3
import json
from lpbook import LPAsyncProxy, LPDriver, LPSyncProxy, LPSyncProxyFromAsyncProxy
from lpbook.error import TemporaryError
from lpbook.execution import HTTP_WEB3_URL
from lpbook.util import LP, Token
from fractions import Fraction as F
from web3.exceptions import BlockNotFound, ContractLogicError

from lpbook.web3 import BlockId, TokenDB
from lpbook.web3.block_stream import BlockStream

logger = logging.getLogger(__name__)

@dataclass
class Reserve:
    real_col: int
    imaginary_col: int
    debt: int
    real_debt: int
    imaginary_debt: int
    max_sell_amount_col: int
    max_sell_amount_debt: int

    def as_dict(self) -> Dict:
        return {
            'real_col': self.real_col,
            'imaginary_col': self.imaginary_col,
            'debt': self.debt,
            'real_debt': self.real_debt,
            'imaginary_debt': self.imaginary_debt,
            'max_sell_amount_col': self.max_sell_amount_col,
            'max_sell_amount_debt': self.max_sell_amount_debt
        }
    
@dataclass
class FluidLP(LP):
    """FluidLP."""
    address: str
    token0: Token
    token1: Token
    reserve0: Reserve
    reserve1: Reserve
    center_price: int
    fee: F

    @classmethod
    @property
    def kind(self) -> str:
        return 'Fluid'

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Fluid'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '1'

    @property
    def tokens(self) -> List[Token]:
        return [self.token0, self.token1]

    @property
    def uid(self) -> str:
        return self.address

    @property
    def gas_stats(self) -> Dict:
        return {
            'mean': 100000, # FIXME
        }

    @property
    def state(self) -> Dict:
        return {
            'reserves': [self.reserve0.as_dict(), self.reserve1.as_dict()],
            'center_price': self.center_price,
            'fee': self.fee
        }
    

def get_main_contract(w3):
    reserves_resolver_address = "0xb387f9C2092cF7c4943F97842887eBff7AE96EB3"
    with open(Path(__file__).parent / 'artifacts' / 'FluidDexReservesResolver.abi', 'r') as f:
        contract_abi = f.read()
    return w3.eth.contract(abi=contract_abi, address=reserves_resolver_address)

class FluideWeb3AsyncProxy(LPAsyncProxy):
    """"Proxies the state of the fluid LP through web3."""

    reserves_resolver_address = "0xb387f9C2092cF7c4943F97842887eBff7AE96EB3"

    def __init__(self, lp_ids, web3_client, token_db: TokenDB):
        self.lp_ids = lp_ids
        self.web3_client = web3_client
        self.token_db = token_db
        self.reserves_resolver_contract = get_main_contract(self.web3_client)

    async def latest_block(self) -> BlockId:
        block = await self.web3_client.eth.get_block()
        return BlockId.from_web3(block)

    @alru_cache
    async def create_all_pools_from_blockchain(self, block: BlockId) -> Dict[str, FluidLP]:
        block_identifier = block.to_web3()
        pools = await self.reserves_resolver_contract.functions.getAllPoolsReserves().call(block_identifier=block_identifier)
        r = {}
        for pool in pools:
            address = pool[0].lower()
            if address not in self.lp_ids:
                continue
            token0 = await self.token_db.get(pool[1].lower())
            if token0 is None:
                continue
            token1 = await self.token_db.get(pool[2].lower())
            if token1 is None:
                continue
            fee = F(pool[3], 1000000)
            center_price = pool[4]
            real_col_0, real_col_1, imaginary_col_0, imaginary_col_1 = pool[5]
            debt_0, debt_1, real_debt_0, real_debt_1, imaginary_debt_0, imaginary_debt_1 = pool[6]

            col_enabled = real_col_0 > 0 and real_col_1 > 0 and imaginary_col_0 > 0 and imaginary_col_1 > 0
            debt_enabled = real_debt_0 > 0 and real_debt_1 > 0 and imaginary_debt_0 > 0 and imaginary_debt_1 > 0

            if not col_enabled and not debt_enabled:
                continue

            widthrawable0, widthrawable1, borrowable0, borrowable1 = pool[7]

            r[address] = FluidLP(
                address=address,
                token0=token0,
                token1=token1,
                reserve0=Reserve(
                    real_col=real_col_0, 
                    imaginary_col=imaginary_col_0, 
                    debt=debt_0, 
                    real_debt=real_debt_0,
                    imaginary_debt=imaginary_debt_0, 
                    max_sell_amount_col=widthrawable0[0], 
                    max_sell_amount_debt=borrowable0[0]
                ),
                reserve1=Reserve(
                    real_col=real_col_1, 
                    imaginary_col=imaginary_col_1, 
                    debt=debt_1, 
                    real_debt=real_debt_1,
                    imaginary_debt=imaginary_debt_1, 
                    max_sell_amount_col=widthrawable1[0], 
                    max_sell_amount_debt=borrowable1[0]
                ),
                center_price=center_price,
                fee=fee
            )
        return r

    async def __call__(
        self,
        block: BlockId
    ) -> Dict[str, LP]:

        logger.debug(
            f'Retrieving uni v2 like state from blockchain at block {block} ...'
        )

        try:
            return await self.create_all_pools_from_blockchain(block)
        except BlockNotFound as e:
            raise TemporaryError(str(e))
        except ContractLogicError as e:
            logger.error(
                f"Transaction reverted when querying fluid."
            )
            raise e
        except ValueError as e:
            if e.args[0]['code'] == -32000:
                raise TemporaryError(str(e))
            raise e

    
class FluidDriver(LPDriver):
    def __init__(
        self,
        block_stream: BlockStream,
        token_db: TokenDB,
        web3_client=None
    ):
        super().__init__(FluidLP)
        self.block_stream = block_stream
        self.token_db = token_db
        self.web3_client = web3_client
        self.reserves_resolver_contract = get_main_contract(self.web3_client)

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:

        assert data_source == LPDriver.LPSyncProxyDataSource.Web3 or LPDriver.LPSyncProxyDataSource.Default
        async_proxy = FluideWeb3AsyncProxy(lp_ids, self.web3_client, self.token_db)
        sync_proxy = LPSyncProxyFromAsyncProxy(
            async_proxy, self.block_stream
        )
        return sync_proxy


    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        self.reserves_resolver_contract = get_main_contract(self.web3_client)
        pools = await self.reserves_resolver_contract.functions.getAllPoolsReserves().call(block_identifier="latest")
        token_ids = set(token_ids)
        return [
            pool[0].lower()
            for pool in pools
            if pool[1].lower() in token_ids and pool[2].lower() in token_ids
        ]
    

async def test():
    HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
    w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(HTTP_WEB3_URL))

    reserves_resolver_address = "0xb387f9C2092cF7c4943F97842887eBff7AE96EB3"
    with open(Path(__file__).parent / 'artifacts' / 'FluidDexReservesResolver.abi', 'r') as f:
        contract_abi = f.read()
    ReservesResolver = w3.eth.contract(abi=contract_abi, address=reserves_resolver_address)
    r = await ReservesResolver.functions.getAllPoolsReserves().call(block_identifier="latest")
    print(json.dumps(r))

if __name__ == '__main__':
    asyncio.run(test())
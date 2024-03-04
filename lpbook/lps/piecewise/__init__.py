
import asyncio
import logging
from dataclasses import dataclass
from typing import Dict, List, Tuple

import aiohttp
from lpbook import (LPDriver,
                    LPSyncProxy)
from lpbook.util import LP, Token
from lpbook.web3 import BlockId

logger = logging.getLogger(__name__)

@dataclass
class PiecewiseLP(LP):
    """PiecewiseLP."""
    buy_token: Token
    sell_token: Token
    points: List[Tuple[float,float]]

    @property
    def tokens(self) -> List[Token]:
        return [self.buy_token, self.sell_token]

    @property
    def uid(self) -> str:
        return f'{self.protocol_name}-v{self.protocol_version}-{self.buy_token.address}-{self.sell_token.address}'

    @property
    def state(self) -> Dict:
        return {
            'buy_token': self.buy_token,
            'sell_token': self.sell_token,
            'points': self.points
        }

@dataclass
class NativeLP(PiecewiseLP):
    """Native market maker."""
    min_buy_amount: float

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Native'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '1'

    @classmethod
    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/3270141 .
        return {    
            'nr_obs': 50,
            'mean': 365052,
            'stddev': 306782,
            'min': 143480,
            'max': 2260914,
            'median': 282865
        }

@dataclass
class HashflowLP(PiecewiseLP):
    """Hashflow market maker."""
    market_maker: str

    @property
    def uid(self) -> str:
        return f'{self.protocol_name}-v{self.protocol_version}-{self.market_maker}-{self.buy_token.address}-{self.sell_token.address}'

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Hashflow'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'

    @classmethod
    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/3270189 .
        return {
            'nr_obs': 1380,
            'mean': 113657,
            'stddev': 25992,
            'min': 27895,
            'max': 289624,
            'median': 114870
        }

PiecewiseLP.as_native = lambda self: NativeLP(**self.__dict__)
PiecewiseLP.as_hashflow = lambda self: HashflowLP(**self.__dict__)

# checks if pieces are monotonically increasing and concave (within tolerance)
def is_monotonically_increasing_and_concave(piecewise_lp):
    def slope_intercept(xy1, xy2):
        m = (xy2[1] - xy1[1]) / (xy2[0] - xy1[0])
        b = xy1[1] - m * xy1[0]
        return m, b

    rel_eps = 1/1000
    points = piecewise_lp.points
    for i in range(1, len(points)):
        if points[i - 1][1] / points[i][1] > 1 + rel_eps:
            return False
        points[i] = (points[i][0], max(points[i][1], points[i-1][1]))
        if i == 1:
            continue
        prev_m, prev_b = slope_intercept(points[i - 2], points[i - 1])
        m, b = slope_intercept(points[i - 1], points[i])
        if m / prev_m > 1 + rel_eps:
            return False
        points[i] = (points[i][0], min(m * points[i][0] + b, prev_m * points[i][0] + prev_b))

    return True

class NativeOrderbook:
    API_KEY='ef46736c46a9a2ed13b42e8ba7a65c2976f17029'
    ORDERBOOK_URL = "https://newapi.native.org/v1/orderbook"
    TOKENS_URL = "https://newapi.native.org/v1/widget-tokens"

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.pools = {}
        self.tokens = None

    async def collect_token_decimals(self):
        async with self.session.get(self.TOKENS_URL, params={'chain':'ethereum'}, headers={'apiKey':self.API_KEY}) as r:
            data = await r.json()
        self.tokens = {}
        for token in data:
            self.tokens[token["address"].lower()] = Token(address=token["address"].lower(), decimals=token["decimals"], symbol=token["symbol"]) 

    def update(self, data):
        self.pools = {}
        for pool in data:
            if pool['side'] == 'bid':
                sell_token = pool['quote_address']
                buy_token = pool['base_address']
                min_buy_amount = pool['minimum_in_base']
            else:
                assert pool['side'] == 'ask'
                sell_token = pool['base_address']
                buy_token = pool['quote_address']
                logger.error("Native piecewise 'ask' pool not supported.")
                continue  # Currently there is no ask quotes in the piecewise - I assume there will be a "minimum_in_quote" field.
            
            if sell_token not in self.tokens or buy_token not in self.tokens:
                continue    # FIXME: apparently some tokens in the piecewise are not in widget-tokens :(

            if len(pool['levels']) == 0:
                continue
            last_x = 0
            last_y = 0
            points = [(0, 0)]
            for level in pool['levels']:
                dx, m = level
                x = last_x + dx
                b = last_y - m * last_x
                y = m * x + b
                points.append((x, y))
                last_x = x
                last_y = y

            pool = NativeLP(
                buy_token=self.tokens[buy_token],
                sell_token=self.tokens[sell_token],
                points=points,
                min_buy_amount=min_buy_amount
            )
            if is_monotonically_increasing_and_concave(pool):
                self.pools[pool.uid] = pool 

    async def poll(self):
        if self.tokens is None:
            await self.collect_token_decimals()
        async with self.session.get(self.ORDERBOOK_URL, params={'chain':'ethereum'}, headers={'apiKey':self.API_KEY}) as r:
            data = await r.json()
        self.update(data)

    async def run_loop(self):
        self.running = True
        logger.info("Starting Native orderbook ...")
        while self.running:
            await self.poll()
            await asyncio.sleep(5)
        logger.info("Stopped Native orderbook.")


class HashflowOrderbook:
    API_KEY='CJWtpFknteKh3xEIVXMEJNAUkf4MUO'
    MARKET_MAKERS_URL='https://api.hashflow.com/taker/v3/market-makers'
    PRICE_LEVELS_URL='https://api.hashflow.com/taker/v3/price-levels'

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.pools = {}
        self.tokens = None
        
    def update(self, market_makers):
        self.pools = {}
        for market_maker, pools in market_makers.items():
            for pool in pools:
                buy_token = Token(
                    address=pool["pair"]["baseToken"],
                    symbol=pool["pair"]["baseTokenName"],
                    decimals=pool["pair"]["baseTokenDecimals"]
                )
                sell_token = Token(
                    address=pool["pair"]["quoteToken"],
                    symbol=pool["pair"]["quoteTokenName"],
                    decimals=pool["pair"]["quoteTokenDecimals"]
                )

                if len(pool['levels']) == 0:
                    continue

                last_x = 0
                last_y = 0
                points = [(0, 0)]

                # For some reason sometimes there is a (0,0) in the first position of the levels array.
                if float(pool['levels'][0]['q'].lower()) == 0 or float(pool['levels'][0]['p'].lower()) == 0:
                    pool['levels'] = pool['levels'][1:]

                for level in pool['levels']:
                    dx, m = float(level['q'].lower()), float(level['p'].lower())
                    x = last_x + dx
                    b = last_y - m * last_x
                    y = m * x + b
                    points.append((x, y))
                    last_x = x
                    last_y = y

                pool = HashflowLP(
                    buy_token=buy_token,
                    sell_token=sell_token,
                    points=points,
                    market_maker=market_maker
                )
                if is_monotonically_increasing_and_concave(pool):
                    self.pools[pool.uid] = pool

    async def poll(self):
        params = [
            ('source', 'quasilabs'),
            ('baseChainType', 'evm'),
            ('baseChainId', '1'),            
        ]
        blacklisted_mms = set()
        headers={'Authorization': self.API_KEY}
        # get market makers        
        async with self.session.get(self.MARKET_MAKERS_URL, params=params, headers=headers) as r:
            market_makers = set((await r.json())["marketMakers"])

        for mm in market_makers - blacklisted_mms:
            params.append(('marketMakers', mm))
        # get pools 
        async with self.session.get(self.PRICE_LEVELS_URL, params=params, headers=headers) as r:
            data = await r.json()
        assert data["status"] == "success"        
        self.update(data["levels"])

    async def run_loop(self):
        self.running = True
        logger.info("Starting Hashflow orderbook ...")
        while self.running:
            await self.poll()
            await asyncio.sleep(5)
        logger.info("Stopped Hashflow orderbook.")


class PiecewiseProxy(LPSyncProxy):
    def __init__(self, orderbook, lp_ids):
        self.orderbook = orderbook
        self.lp_ids = lp_ids

    def __call__(self, block: BlockId) -> Dict[str, LP]:
        """Returns the recent state if synced, or an error otherwise."""
        p = {id: pool for id, pool in self.orderbook.pools.items() if id in self.lp_ids}
        return p

    async def start(self) -> None:
        """Starts syncing proxy with proxied data source."""
        self.run_loop_task = asyncio.create_task(self.orderbook.run_loop())

    def stop(self) -> None:
        """Stops syncing proxy with proxied data source."""
        self.orderbook.running = False
        self.run_loop_task.cancel()

class PiecewiseDriver(LPDriver):
    def __init__(
        self,
        orderbook
    ):
        super().__init__(PiecewiseLP)
        self.orderbook = orderbook
        self.token_pairs = None

    def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        return PiecewiseProxy(self.orderbook, lp_ids)

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        await self.orderbook.poll() 
        r = [
            id
            for id, pool in self.orderbook.pools.items()
                if pool.buy_token.address in token_ids and pool.sell_token.address in token_ids
        ]
        return r

class NativeDriver(PiecewiseDriver):
    def __init__(
        self,
        session: aiohttp.ClientSession
    ):
        orderbook = NativeOrderbook(session)
        super().__init__(orderbook)

class HashflowDriver(PiecewiseDriver):
    def __init__(
        self,
        session: aiohttp.ClientSession
    ):
        orderbook = HashflowOrderbook(session)
        super().__init__(orderbook)


import asyncio
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import datetime

import aiohttp
import websockets
import json

from lpbook import (LPDriver,
                    LPSyncProxy)
from lpbook.util import LP, Token
from lpbook.web3 import BlockId, TokenDB
from math import floor, ceil
import web3 
from collections import namedtuple
from copy import deepcopy

logger = logging.getLogger(__name__)

@dataclass
class PiecewiseLP(LP):
    """PiecewiseLP."""
    buy_token: Token
    sell_token: Token
    points: List[Tuple[float,float]]

    @classmethod
    @property
    def kind(self) -> str:
        return 'Piecewise'

    @property
    def tokens(self) -> List[Token]:
        return [self.buy_token, self.sell_token]

    @property
    def uid(self) -> str:
        return f'{self.protocol_name}_{self.protocol_version}-{self.buy_token.address}-{self.sell_token.address}'

    @property
    def state(self) -> Dict:
        return {
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

    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/3270141 .
        return {    
            'mean': 365052,
            'stddev': 306782,
        }

@dataclass
class HashflowLP(PiecewiseLP):
    """Hashflow market maker."""
    market_maker: str

    @property
    def uid(self) -> str:
        return f'{self.protocol_name}_{self.protocol_version}-{self.market_maker}-{self.buy_token.address}-{self.sell_token.address}'

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Hashflow'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'

    @property
    def gas_stats(self) -> Dict:
        # See https://dune.com/queries/3270189 .
        return {
            'mean': 113657,
            'stddev': 25992,
        }

@dataclass
class BebopLP(PiecewiseLP):
    last_updated: datetime

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Bebop'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'

    @property
    def gas_stats(self) -> Dict:
        # FIXME: todo
        return {
            'mean': 113657,
            'stddev': 25992,
        }

@dataclass
class ZeroExLP(PiecewiseLP):

    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'ZeroEx'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '4'

    @property
    def gas_stats(self) -> Dict:
        # FIXME: todo
        return {
            'mean': 113657,
            'stddev': 25992,
        }
    
PiecewiseLP.as_native = lambda self: NativeLP(**self.__dict__)
PiecewiseLP.as_hashflow = lambda self: HashflowLP(**self.__dict__)
PiecewiseLP.as_zeroex = lambda self: ZeroExLP(**self.__dict__)

def slope_intercept(xy1, xy2):
    m = (xy2[1] - xy1[1]) / (xy2[0] - xy1[0])
    b = xy1[1] - m * xy1[0]
    return m, b

# checks if pieces are monotonically increasing and concave (within tolerance)
def is_monotonically_increasing_and_concave(piecewise_lp):
    rel_eps = 1/1000
    points = piecewise_lp.points
    for i in range(1, len(points)):
        if points[i][1] == 0 or points[i - 1][1] / points[i][1] > 1 + rel_eps:
            return False
        points[i] = (points[i][0], max(points[i][1], points[i - 1][1]))
        if i == 1:
            continue
        prev_m, prev_b = slope_intercept(points[i - 2], points[i - 1])
        m, b = slope_intercept(points[i - 1], points[i])
        if m / prev_m > 1 + rel_eps:
            return False
        points[i] = (points[i][0], min(m * points[i][0] + b, prev_m * points[i][0] + prev_b))

    return True

# "floors" curve so that it is monotonically increasing and concave. 
# Returns None if not possible (just because currently because curve need to start at (0,0) )
# NOTE: Points are unscaled (we are in the integer world here) 
def make_monotonically_increasing_and_concave(piecewise_lp) -> Optional[PiecewiseLP]:
    points = piecewise_lp.points
    # go from right to left, and try to make it monotonically increasing
    for i in reversed(range(1, len(points))):
        if points[i][1] == 0:
            return None
        points[i - 1] = (points[i - 1][0], min(points[i - 1][1], points[i][1]))

    # go from left to right, and try to make it concave   
    for i in range(2, len(points)):
        prev_m, prev_b = slope_intercept(points[i - 2], points[i - 1])
        points[i] = (points[i][0], min(points[i][1], ceil(prev_m * points[i][0] + prev_b)))

    piecewise_lp = deepcopy(piecewise_lp)
    piecewise_lp.points = points
    return piecewise_lp

# Returns None if resulting curve differs to much from passed curve
def make_monotonically_increasing_and_concave_within_tol(piecewise_lp, rel_tol) -> Optional[PiecewiseLP]:
    fixed_lp = make_monotonically_increasing_and_concave(piecewise_lp)
    if fixed_lp is None:
        return fixed_lp
    for i in range(1, len(fixed_lp.points)):
        x, y = piecewise_lp.points[i]
        fixed_x, fixed_y = fixed_lp.points[i]
        assert x == fixed_x
        assert fixed_y <= y
        if y / fixed_y > 1 + rel_tol:
            return None
    return fixed_lp 

# Remove some pieces if doing so does not change curve too much
def simplify(piecewise_lp, rel_tol) -> PiecewiseLP:
    points = piecewise_lp.points
    while len(points) > 2:
        # find candidate removals
        candidate_removals = []
        for i in range(0, len(points) - 2):
            m, b = slope_intercept(points[i], points[i + 2])
            x1, y1 = points[i + 1]
            new_y1 = floor(x1 * m + b)  
            if y1 >= new_y1 and y1 / new_y1 <= 1 + rel_tol:
                candidate_removals.append((i + 1, y1 / new_y1))
        if len(candidate_removals) == 0:
            break 
        i_to_remove = min(candidate_removals, key=lambda ie: ie[1])[0]
        points = [points[i] for i in range(len(points)) if i != i_to_remove]

    piecewise_lp = deepcopy(piecewise_lp)
    piecewise_lp.points = points
    return piecewise_lp

class NativeOrderbook:
    API_KEY='ef46736c46a9a2ed13b42e8ba7a65c2976f17029'
    ORDERBOOK_URL = "https://newapi.native.org/v1/orderbook"
    TOKENS_URL = "https://newapi.native.org/v1/widget-tokens"

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.pools = {}
        self.tokens = None

    async def async_init(self):
        await self.poll()

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

            x_scale = 10**self.tokens[buy_token].decimals
            y_scale = 10**self.tokens[sell_token].decimals
            points = [(ceil(x * x_scale), floor(y * y_scale)) for (x, y) in points]

            pool = NativeLP(
                buy_token=self.tokens[buy_token],
                sell_token=self.tokens[sell_token],
                points=points,
                min_buy_amount=min_buy_amount
            )
            # FIXME: native sometimes has a min_buy_amount encoded in the curve, e.g. the first
            # segment is (0,0)-(100000,0), which is non concave. This could be fixed by removing
            # these segments from the curve, and adding support for an amm min buy amount in the 
            # solver.
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
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.pools = {}

    async def async_init(self):
        await self.poll()

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

                x_scale = 10**buy_token.decimals
                y_scale = 10**sell_token.decimals
                points = [(ceil(x * x_scale), floor(y * y_scale)) for (x, y) in points]

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
        #whitelisted_mms = {"mm21_1", "mm29_5"}
        blacklisted_mms = {
            "mm18_1",  # rate limited
            "mm12_1",   # invalid input
            "mm9_1"     # no maker supports this request
        }
        headers={'Authorization': self.API_KEY}
        # get market makers        
        async with self.session.get(self.MARKET_MAKERS_URL, params=params, headers=headers) as r:
            market_makers = set((await r.json())["marketMakers"])
        for mm in market_makers  - blacklisted_mms:
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


class BebopOrderbook:
    API_USER='quasilabs'
    API_KEY='bd64037e-2081-4e77-8be8-73857762c9f2'
    WSS_PRICING_URL='wss://api.bebop.xyz/pmm/ethereum/v3/pricing'

    def __init__(self, token_db: TokenDB):
        self.token_db = token_db
        self.session = aiohttp.ClientSession()
        self.pools = {}
        self.last_updated = {}

    async def async_init(self):
        await self.run_once()

    async def run_once(self):
        async with websockets.connect(self.WSS_PRICING_URL, extra_headers={"name": self.API_USER, "Authorization": self.API_KEY}) as ws:
            message = await ws.recv()
            message = json.loads(message)
            for k, v in message.items():
                await self.update_pools(k, v)

    async def run_loop(self):
        self.running = True
        logger.info("Starting Bebop orderbook ...")
        async with websockets.connect(self.WSS_PRICING_URL, extra_headers={"name": self.API_USER, "Authorization": self.API_KEY}) as ws:
            while self.running:
                message = await ws.recv()
                message = json.loads(message)
                for k, v in message.items():
                    await self.update_pools(k, v)
        logger.info("Stopped Bebop orderbook.")
    
    async def update_pools(self, tp_str, data):
        last_update = datetime.datetime.fromtimestamp(data["last_update_ts"], datetime.UTC)
        if tp_str in self.last_updated and self.last_updated[tp_str] == last_update:
            return

        self.last_updated[tp_str] = last_update

        base_token_address, quote_token_address = tp_str.lower().split("/")
        base_token = await self.token_db.get(base_token_address)
        quote_token = await self.token_db.get(quote_token_address)

        if base_token is None or quote_token is None:
            return

        # bid = pool buys base token, ask = pool sells base token
        pool1 = self.create_pool_from_bids(base_token, quote_token, data["bids"], last_update)
        pool2 = self.create_pool_from_asks(quote_token, base_token, data["asks"], last_update)

        pool1pts = pool1.points
        pool2pts = pool2.points

        pool1_id = f'{BebopLP.protocol_name}_{BebopLP.protocol_version}-{base_token.address}-{quote_token.address}'
        pool2_id = f'{BebopLP.protocol_name}_{BebopLP.protocol_version}-{quote_token.address}-{base_token.address}'

        pool1 = make_monotonically_increasing_and_concave_within_tol(pool1, 0.0001)

        if pool1 is not None:
            pool1pts_before_simp = pool1.points
            self.pools[pool1_id] = simplify(pool1, 0.0001)
            if self.pools[pool1_id].points[0][0] != 0:
                print(self.pools[pool1_id].points, "\n", pool1pts, "\n", pool1pts_before_simp)
                import sys
                sys.exit(0)

        pool2 = make_monotonically_increasing_and_concave_within_tol(pool2, 0.0001)

        if pool2 is not None:
            pool2pts_before_simp = pool2.points
            self.pools[pool2_id] = simplify(pool2, 0.0001)
            if self.pools[pool2_id].points[0][0] != 0:
                print(self.pools[pool2_id].points, "\n", pool2pts, "\n", pool2pts_before_simp)
                import sys
                sys.exit(0)


    def scale(self, buy_token, sell_token, points):
        x_dec = 10**buy_token.decimals
        y_dec = 10**sell_token.decimals
        return [(ceil(x * x_dec), floor(y * y_dec)) for x, y in points]

    def create_pool_from_bids(self, buy_token, sell_token, data, last_update):
        points = [(0, 0)]
        for y_over_x, x in data:
            y = y_over_x * x
            last_x, last_y = points[-1]
            points.append((x + last_x, y + last_y))
        points = self.scale(buy_token, sell_token, points)
        return BebopLP(buy_token=buy_token, sell_token=sell_token, points=points, last_updated=last_update)

    def create_pool_from_asks(self, buy_token, sell_token, data, last_update):
        points = [(0, 0)]
        for x_over_y, y in data:
            x = x_over_y * y
            last_x, last_y = points[-1]
            points.append((x + last_x, y + last_y))
        points = self.scale(buy_token, sell_token, points)
        return BebopLP(buy_token=buy_token, sell_token=sell_token, points=points, last_updated=last_update)

class ZeroExOrderbook:
    API_KEY='e4c12e27-4aeb-46a6-b594-725a6b829c23'
    HTTPS_URL='https://api.0x.org/orderbook/v1/orders'
    WSS_URL='wss://api.0x.org/orderbook/v1'

    BuyOrder = namedtuple('ZeroExBuyOrder', ['buy_token', 'sell_token', 'buy_amount', 'sell_amount', 'fee', 'hash', 'expiry'])

    def __init__(self, token_db: TokenDB):
        self.token_db = token_db
        self.session = aiohttp.ClientSession()
        self.pools = {}

    async def async_init(self):
        orders = await self.fetch_orderbook()
        self.create_pools(orders)

    def order_is_almost_expiring(self, o):
        expiry_dt = datetime.datetime.fromtimestamp(min(10000000000, o.expiry), tz=datetime.UTC)
        return expiry_dt <= datetime.datetime.now(tz=datetime.UTC) + datetime.timedelta(minutes=1)
    
    def order_is_fullfilled(self, o):
        return o.buy_amount == 0
    
    async def create_order_from_record(self, record) -> Optional[BuyOrder]:
        order = record["order"]
        metadata = record["metaData"]
        if order["taker"] != "0x0000000000000000000000000000000000000000":
            return None
        if order["chainId"] != 1:
            return None
        expiry = int(order["expiry"])
        sell_token = order["makerToken"]
        buy_token = order["takerToken"]
        remaining_buy_amount = int(metadata["remainingFillableTakerAmount"])
        sell_amount = int(order["makerAmount"])
        buy_amount = int(order["takerAmount"])
        fee_recipient = order["feeRecipient"]
        fee = int(order["takerTokenFeeAmount"])
        hash = metadata["orderHash"]

        sell_amount = floor(remaining_buy_amount * sell_amount / buy_amount)
        buy_amount = remaining_buy_amount
        
        buy_token = await self.token_db.get(buy_token)
        sell_token = await self.token_db.get(sell_token)

        if buy_token is None or sell_token is None:
            return None

        return self.BuyOrder(buy_token=buy_token, sell_token=sell_token, buy_amount=buy_amount, sell_amount=sell_amount, fee=fee, hash=hash, expiry=expiry)
                    
    async def fetch_orderbook(self):
        page=1
        per_page=1000
        records = []
        while True:
            async with self.session.get(self.HTTPS_URL, params={'page':str(page), 'perPage':str(per_page)}, headers={'0x-api-key': self.API_KEY}) as r:
                data = await r.json()
            records += data["records"]
            page += 1
            logger.debug(f"Retrieved {len(records)}/{data['total']} records from ZeroEx orderbook.")
            if len(data["records"]) < per_page:
                break
        orders = []
        for record in records:
            order = await self.create_order_from_record(record)
            if order is None:
                continue
            orders.append(order)
        return orders

    def filter_orders(self, orders):
        # Filter out unwanted orders
        return list(filter(lambda o: not self.order_is_almost_expiring(o) and not self.order_is_fullfilled(o), orders))

    def create_pool(self, buy_token, sell_token, orders):
        # sort by best-to-worse price (for taker)
        orders = sorted(orders, key=lambda o: o.sell_amount/(o.buy_amount + o.fee), reverse=True)
        last_x = 0
        last_y = 0
        points = [(0, 0)]
        for order in orders:
            last_x += order.buy_amount + order.fee  # FIXME: make sure
            last_y += order.sell_amount
            points.append((last_x, last_y))
        return ZeroExLP(buy_token=buy_token, sell_token=sell_token, points=points)
    
    def create_pools(self, orders):
        self.orders_by_token_pair = {}
        self.order_hashes = set()
        for order in orders:
            self.orders_by_token_pair.setdefault((order.buy_token, order.sell_token),[]).append(order)
            self.order_hashes.add(order.hash)
        for buy_sell_tokens, orders in self.orders_by_token_pair.items():
            buy_token, sell_token = buy_sell_tokens
            orders = self.filter_orders(orders)
            if len(orders) == 0:
                continue
            pool = self.create_pool(buy_token=buy_token, sell_token=sell_token, orders=orders)
            if is_monotonically_increasing_and_concave(pool):
                self.pools[pool.uid] = pool
    
    # Returns True if order was indeed added, or False if already exist 
    def add_order(self, o) -> bool:
        if o.hash in self.order_hashes:
            return False
        self.order_hashes.add(o.hash)        
        self.orders_by_token_pair.setdefault((o.buy_token, o.sell_token), []).append(o)
        return True

    # Returns True if order was indeed removed, or False if did not exist
    def remove_order(self, o) -> bool:
        if o.hash not in self.order_hashes:
            return False
        self.order_hashes.remove(o.hash)        
        self.orders_by_token_pair[o.buy_token, o.sell_token] = list(o1 for o1 in self.orders_by_token_pair[o.buy_token, o.sell_token] if o1.hash!=o.hash)
        return True

    def update_pools(self, orders_to_add, orders_to_remove):
        updated_token_pairs = set()
        for o in orders_to_remove:
            if self.remove_order(o):
                updated_token_pairs.add((o.buy_token, o.sell_token))
        for o in orders_to_add:
            if self.add_order(o):
                updated_token_pairs.add((o.buy_token, o.sell_token))
        for buy_token, sell_token in updated_token_pairs:
            orders = self.orders_by_token_pair[buy_token, sell_token]
            orders = self.filter_orders(orders)
            if len(orders) == 0:
                continue
            pool = self.create_pool(buy_token=buy_token, sell_token=sell_token, orders=orders)
            if is_monotonically_increasing_and_concave(pool):
                self.pools[pool.uid] = pool

    async def run_loop(self):
        self.running = True
        logger.info("Starting ZeroEx orderbook ...")
        await self.async_init()  # Run this again to make sure time gap between switching HTTP/WS interfaces is minimal
        async with websockets.connect(self.WSS_URL) as ws:
            await ws.send(json.dumps({
                'type': 'subscribe',
                'channel': 'orders',
                'requestId': 'quasilabs'
            }))

            while self.running:
                message = await ws.recv()
                message = json.loads(message)
                assert(message["type"] == "update")
                assert(message["channel"] == "orders")
                orders_to_add = []
                orders_to_remove = []
                for record in message["payload"]:
                    state = record["metaData"]["state"]
                    order = await self.create_order_from_record(record)
                    if order is None:
                        continue
                    if state == "ADDED":
                        orders_to_add.append(order)
                    elif state in {"EXPIRED", "CANCELLED"}:
                        orders_to_remove.append(order)
                    elif state == "FILLABLE":
                        print("FILLABLE", order)
                        for orders in self.orders_by_token_pair.values():
                            for o in orders:
                                if o.hash == order.hash:
                                    print("previous:", o)
                        orders_to_remove.append(order)
                        orders_to_add.append(order)
                    else:
                        raise RuntimeError(f"Unexpected ZeroEx delta {state}.")
                self.update_pools(orders_to_add, orders_to_remove)
        logger.info("Stopped ZeroEx orderbook.")

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
        async def run_loop():
            while True:
                try:
                    await self.orderbook.run_loop()
                except Exception:
                    logger.exception("Piecewise proxy unhandled exception. Resetting ...") 
        self.background_task = asyncio.create_task(run_loop())

    def stop(self) -> None:
        """Stops syncing proxy with proxied data source."""
        self.orderbook.running = False

class PiecewiseDriver(LPDriver):
    def __init__(
        self,
        orderbook
    ):
        super().__init__(PiecewiseLP)
        self.orderbook = orderbook
        self.token_pairs = None
        self.async_initialized = False

    async def create_lp_sync_proxy(
        self,
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        return PiecewiseProxy(self.orderbook, lp_ids)

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        if not self.async_initialized:
            await self.orderbook.async_init()
            self.async_initialized = True 
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
        self
    ):
        orderbook = HashflowOrderbook()
        super().__init__(orderbook)

class ZeroExDriver(PiecewiseDriver):
    def __init__(
        self,
        token_db: TokenDB
    ):
        orderbook = ZeroExOrderbook(token_db)
        super().__init__(orderbook)

class BebopDriver(PiecewiseDriver):
    def __init__(
        self,
        token_db: TokenDB
    ):
        orderbook = BebopOrderbook(token_db)
        super().__init__(orderbook)

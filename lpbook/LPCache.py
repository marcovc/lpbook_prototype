import asyncio
import datetime
import gc
from itertools import permutations
import logging
import traceback
from typing import Iterable, List, Optional, Set, Tuple

from lpbook import LPDriver, LPSyncProxy
from lpbook.error import CacheMissError

from lpbook.util import LP, Token, traced, traced_context
from lpbook.web3 import BlockId
import lpbook.util.prometheus as prometheus
import jsonpickle
import time
from lpbook.lp_monitors import lp_monitors
from lpbook.web3.block_stream import BlockStream

logger = logging.getLogger(__name__)


class LPCache:
    POOL_MAX_UNUSED_AGE = datetime.timedelta(days=1)
    POOL_MIN_CACHED_AGE = datetime.timedelta(minutes=10)
    POOL_MAX_CACHED_AGE = datetime.timedelta(days=1)
    POOL_MAX_CACHE_SIZE = 1000

    def __init__(self, lp_drivers, order_drivers, block_stream: BlockStream, state_directory: str, always_include_amms_by_protocol: dict[str, set[str]]={}):
        self.lp_drivers = {driver.uid: driver for driver in lp_drivers}
        self.order_lp_drivers = {driver.uid: driver for driver in order_drivers}
        self.state_directory = state_directory
        self.always_include_amms_by_protocol = always_include_amms_by_protocol
        self.always_include_amms = set()
        for amms in self.always_include_amms_by_protocol.values():
            self.always_include_amms |= amms
        self.cached_tokens = set()
        self.token_last_request_datetime = {}
        self.last_refresh_datetime = None
        
        self.load_state()
        self.background_tasks = set()
        for driver in self.lp_drivers.values():
            driver.subscribe_on_sync(self.on_sync)
        for driver in self.order_lp_drivers.values():
            driver.subscribe_on_sync(self.on_sync)
        
        # This is required since drivers only call sync when they have a proxy, and they only have a proxy
        # when the request tokens can be served by the proxy. By doing this, we will keep a block "heartbeat"
        # even when there is no data to be served.
        async def f(block):
            self.on_sync(block, None)
        block_stream.subscribe(f)

        self.nr_cache_hits = 0
        self.nr_cache_misses = 0

        self.on_sync_subscribers = []

    def __del__(self):
        for driver in self.lp_drivers.values():
            driver.unsubscribe_on_sync(self.on_sync)
        for driver in self.order_lp_drivers.values():
            driver.unsubscribe_on_sync(self.on_sync)
        for task in self.background_tasks:
            task.cancel()

    def subscribe_on_sync(self, subscriber):
        self.on_sync_subscribers.append(subscriber)

    def unsubscribe_on_sync(self, subscriber):
        self.on_sync_subscribers = [s for s in self.on_sync_subscribers if s != subscriber]            

    def load_state(self):
        try:
            with open(self.state_directory / "last_cached_tokens.json", "r") as f:
                last_cached_tokens = jsonpickle.decode(f.read())
                for t in last_cached_tokens:
                    self.token_last_request_datetime[t] = datetime.datetime.now()
        except FileNotFoundError:
            pass

    def dump_state(self):
        # Save only the most used 200 tokens.
        ct = {k for k,_ in sorted(self.token_last_request_datetime.items(), key=lambda kv: kv[1], reverse=True)[:200]}

        with open(self.state_directory / "last_cached_tokens.json", "w+") as f:
            f.write(jsonpickle.encode(ct))
        
    def update_token_ids(self, token_ids: set):
        now = datetime.datetime.now()
        for t in token_ids:
            if t in self.cached_tokens:
                self.nr_cache_hits += 1
            else:
                self.nr_cache_misses += 1
            self.token_last_request_datetime[t] = now

    def get_lps_trading_tokens(self, token_ids: set, block_number=None) -> List[LP]:
        """Return all LPs that trade at least two tokens in token_ids.

        If block is given, then the lp's state will reflect that block if that block is
        in cache, otherwise it will raise a CacheMissError.
        """
        now = datetime.datetime.now()
        for t in token_ids:
            self.token_last_request_datetime[t] = now

        # Always return immediately whatever is cached.
        all_lps = []
        block = BlockId(number=block_number)
        for driver in self.lp_drivers.values():
            try:
                lps = driver.all_lps(block)
            except CacheMissError:
                logger.debug(f'Driver {driver.uid} still initializing. Skipping ...')
                continue
            for lp in lps:
                lp_token_ids = {t.address for t in lp.tokens}
                if len(lp_token_ids & token_ids) >= 2 or lp.uid in self.always_include_amms:
                    all_lps.append(lp)

        if len(all_lps) == 0:
            logger.debug(f'Returning no LPs for {len(token_ids)} requested tokens.')
        else:
            logger.debug(f'Returning {len(all_lps)} LPs.')

        self.nr_cache_hits += len(self.cached_tokens & token_ids)
        self.nr_cache_misses += len(token_ids - self.cached_tokens)

        return all_lps

    def get_all_lps(self, block_number=None) -> List[LP]:
        """Return all cached LPs.

        If block is given, then the lp's state will reflect that block if that block is
        in cache, otherwise it will raise a CacheMissError.
        """
        now = datetime.datetime.now()

        # Always return immediately whatever is cached.
        all_lps = []
        block = BlockId(number=block_number)
        for driver in self.lp_drivers.values():
            try:
                all_lps += driver.all_lps(block)
            except CacheMissError:
                logger.debug(f'Driver {driver.uid} still initializing. Skipping ...')
                continue

        if len(all_lps) == 0:
            logger.debug(f'Returning no LPs.')
        else:
            logger.debug(f'Returning all {len(all_lps)} cached LPs.')

        return all_lps
    
    def get_order_lps(self, block_number=None) -> List[LP]:
        # Always return immediately whatever is cached.
        all_lps = []
        block = BlockId(number=block_number)
        for driver in self.order_lp_drivers.values():
            try:
                lps = driver.all_lps(block)
            except CacheMissError:
                logger.debug(f'Driver {driver.uid} still initializing. Skipping ...')
                continue
            all_lps += lps

        if len(all_lps) == 0:
            logger.debug(f'Returning no orders LPs.')
        else:
            logger.debug(f'Returning {len(all_lps)} order LPs.')
        return all_lps
    
    @traced(logger, 'Running LP cache')
    async def run(self):
        self.running = True

        for driver in self.order_lp_drivers.values():
            await driver.refresh([], set())

        while self.running:
            now = datetime.datetime.now()

            # Prune self.token_last_request_datetime to only have the most recent POOL_MAX_CACHE_SIZE entries.
            self.token_last_request_datetime = {
                k: v 
                for k, v in sorted(self.token_last_request_datetime.items(), key=lambda kv: kv[1], reverse=True)[:self.POOL_MAX_CACHE_SIZE]
            }

            # From those, apply the second cache eviction crieteria, POOL_MAX_UNUSED_AGE.
            most_requested_tokens = {
                t
                for t, dt in self.token_last_request_datetime.items()
                if now - dt <= self.POOL_MAX_UNUSED_AGE
            }

            # Refresh if a) cache doesn't equal most requested tokens or
            # b) if last cache refresh was too long ago.
            # Condition a) handles cache misses and makes sure it is not
            # tracking unused tokens. Condition b) is required since new
            # lps may have been created/deleted for the recently cached
            # tokens since last refresh.
            if (
                len(most_requested_tokens) > 0 and
                self.cached_tokens != most_requested_tokens
            ) or self.last_refresh_datetime is None or \
                    now - self.last_refresh_datetime > self.POOL_MAX_CACHED_AGE:
                await self.refresh(most_requested_tokens)
                self.dump_state()

            await asyncio.sleep(self.POOL_MIN_CACHED_AGE.total_seconds())

    def shutdown(self):
        self.running = False

    @traced(logger, 'Refreshing LP cache')
    async def refresh(self, tokens):
        logger.debug(f'Refreshing LP cache for {len(tokens)} tokens ...')
        now = datetime.datetime.now()         

        if len(tokens) > 0:
            await asyncio.gather(*[
                driver.refresh(tokens, self.always_include_amms_by_protocol.get(driver.protocol, set())) 
                for driver in self.lp_drivers.values()
            ])

        self.cached_tokens = tokens
        self.last_refresh_datetime = now
        gc.collect()

    @classmethod
    def estimate_average_xrate_in_running_hour_for_all_token_pairs(cls, lps: Iterable[LP], block_number: int, block_time: datetime.datetime) -> dict[Tuple[Token, Token], Tuple[float, Optional[float]]]:
        if lp_monitors is None:
            return {}
        token_pairs = set()
        for lp in lps:
            for token_pair in permutations(lp.tokens, 2):
                token_pairs.add(token_pair)
        return lp_monitors.traded_amount_collectors.estimate_average_xrates_in_running_hour(token_pairs, block_number, block_time)
    
    def on_sync(self, block: BlockId, driver: Optional[LPDriver]):
        if driver is not None:
            logger.debug(f'Driver {driver.uid} synced to block {block.number}.')
        if all(d.is_synced_to(block) for d in self.lp_drivers.values()) and \
            all(d.is_synced_to(block) for d in self.order_lp_drivers.values()):
            async def f():
                await asyncio.sleep(0.01)  # yield current task
                logger.debug(f'Synced to new block {block.number}.')
                for subscriber in self.on_sync_subscribers:
                    await subscriber(block)

            task = asyncio.create_task(f())
            self.background_tasks.add(task)
            task.add_done_callback(lambda _: self.background_tasks.remove(task))
        else:
            max_block_number = max([d.latest_sync_block.number for d in self.lp_drivers.values() if d.sync_proxy is not None and d.latest_sync_block is not None], default=None) 
            if max_block_number is None:
                return
            protocols_behind = {
                d.protocol: max_block_number - d.latest_sync_block.number
                for d in self.lp_drivers.values() 
                if d.sync_proxy is not None and d.latest_sync_block is not None and d.latest_sync_block.number <= max_block_number - 2
            }
            if len(protocols_behind) == 0:
                return
            logger.warning(f'Protocols {list(protocols_behind.keys())} are running behind by {list(protocols_behind.values())} blocks respectively.')

    def stats(self):
        return {
            "Tokens": len(self.cached_tokens),
            "Hit rate": self.nr_cache_hits / (self.nr_cache_hits + self.nr_cache_misses) * 100 
                if self.nr_cache_hits + self.nr_cache_misses > 0 else 0,
        }

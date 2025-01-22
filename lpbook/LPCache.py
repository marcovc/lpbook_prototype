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

logger = logging.getLogger(__name__)


class LPCache:
    POOL_MAX_UNUSED_AGE = datetime.timedelta(days=1)
    POOL_MIN_CACHED_AGE = datetime.timedelta(minutes=10)
    POOL_MAX_CACHED_AGE = datetime.timedelta(days=1)
    POOL_MAX_CACHE_SIZE = 1000

    def __init__(self, lp_drivers, order_drivers, state_directory: str, always_include_amms_by_protocol: dict[str, set[str]]={}):
        self.lp_drivers = lp_drivers
        self.order_drivers = order_drivers
        self.state_directory = state_directory
        self.always_include_amms_by_protocol = always_include_amms_by_protocol
        self.always_include_amms = set()
        for amms in self.always_include_amms_by_protocol.values():
            self.always_include_amms |= amms
        self.cached_tokens = set()
        self.token_last_request_datetime = {}
        self.last_refresh_datetime = None
        self.lp_sync_proxies = {}
        self.lp_sync_pool_ids = {}
        self.order_sync_proxies = []
        self.load_state()
        self.background_tasks = set()
        self.driver_latest_block = {}

    def __del__(self):
        for proxy in self.lp_sync_proxies.values():
            proxy.unsubscribe_on_sync(self.on_sync)
        for task in self.background_tasks:
            task.cancel()
            
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
        for lp_sync_proxy in self.lp_sync_proxies.values():
            try:
                lps = list(lp_sync_proxy(block).values())
            except CacheMissError:
                logger.debug(f'LPProxy {lp_sync_proxy} still initializing. Skipping ...')
                continue
            for lp in lps:
                lp_token_ids = {t.address for t in lp.tokens}
                if len(lp_token_ids | token_ids) >= 2 or lp.uid in self.always_include_amms:
                    all_lps.append(lp)

        if len(all_lps) == 0:
            logger.debug(f'No LPs for token_ids {token_ids}.')
        else:
            logger.debug(f'Returning {len(all_lps)} LPs.')
        return all_lps

    def get_order_lps(self, block_number=None) -> List[LP]:
        # Always return immediately whatever is cached.
        all_lps = []
        block = BlockId(number=block_number)
        for order_sync_proxy in self.order_sync_proxies:
            try:
                lps = list(order_sync_proxy(block).values())
            except CacheMissError:
                logger.debug(f'LPProxy {order_sync_proxy} still initializing. Skipping ...')
                continue
            all_lps += lps

        if len(all_lps) == 0:
            logger.debug(f'No orders LPs.')
        else:
            logger.debug(f'Returning {len(all_lps)} order LPs.')
        return all_lps

    def get_lps(self, lp_ids: Set[str], block_number=None) -> List[LP]:
        """Return the set of LPs with the given ids. Raise CacheMissError if not found.

        If block is given, then the lp's state will reflect that block if that block is
        in cache, otherwise it will raise a CacheMissError.
        """
        # Always return immediately whatever is cached.
        all_lps = []
        block = BlockId(number=block_number)
        for lp_sync_proxy in self.lp_sync_proxies.values():
            try:
                lps = list(lp_sync_proxy(block).values())
            except CacheMissError:
                logger.debug(f'LPProxy {lp_sync_proxy} still initializing. Skipping ...')
                continue
            all_lps += [lp for lp in lps if lp.uid in lp_ids]

        if len(all_lps) < len(lp_ids):
            raise CacheMissError(f'Could not find LPs {lp_ids - set([lp.uid for lp in all_lps])} in cache.')
        else:
            logger.debug(f'Returning all {len(all_lps)} requested LPs.')
        return all_lps
    
    @traced(logger, 'Running LP cache')
    async def run(self):
        self.running = True

        for driver in self.order_drivers:
            self.order_sync_proxies.append(await self.create_order_lp_sync_proxy(driver))

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

    async def create_order_lp_sync_proxy(self, driver):
        lp_ids = await driver.get_lp_ids([])
        new_order_lp_sync_proxy = await driver.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.Default
        )

        try:
            await new_order_lp_sync_proxy.start()
        except Exception as err:
            logger.error(
                f"Error starting order lp sync proxy for {driver.uid}: {err}. "
                f"Traceback:\n{traceback.format_exc()}"
            )
            prometheus.refresh_driver_error.labels(protocol=driver.uid).inc(1)

        return new_order_lp_sync_proxy

    async def refresh_driver(self, driver, tokens):
        cur_lp_sync_proxy = self.lp_sync_proxies.get(driver.uid, None)
        cur_lp_ids = self.lp_sync_pool_ids.get(driver.uid, set())

        try:
            new_lp_ids = set(await driver.get_lp_ids(tokens)) | self.always_include_amms_by_protocol.get(driver.protocol, set())
        except Exception:
            logger.exception(f"Error querying lps for {driver.uid}.")
            prometheus.refresh_driver_error.labels(protocol=driver.uid).inc(1)
            # Keep current proxy in case of error
            return (cur_lp_sync_proxy, cur_lp_ids)

        if len(new_lp_ids) == 0:
            class NoOpSyncProxy:
                def __call__(self, _):
                    return {}

                async def stop(self):
                    pass

            return (NoOpSyncProxy(), set())

        # optimization: no need to reset proxies that return
        # the same set of pools as last time.
        if new_lp_ids == cur_lp_ids:
            return (cur_lp_sync_proxy, cur_lp_ids)

        new_lp_sync_proxy = await driver.create_lp_sync_proxy(
                new_lp_ids,
                LPDriver.LPSyncProxyDataSource.Default
            )

        try:
            logger.debug(f"Starting sync proxy for {driver.uid} because {len(new_lp_ids - cur_lp_ids)} lp_ids were added and {len(cur_lp_ids - new_lp_ids)} were deleted")
            await new_lp_sync_proxy.start()
        except Exception:
            logger.exception(f"Error starting lp sync proxy for {driver.uid}")
            prometheus.refresh_driver_error.labels(protocol=driver.uid).inc(1)
            return (cur_lp_sync_proxy, cur_lp_ids)

        return (new_lp_sync_proxy, new_lp_ids)

    @traced(logger, 'Refreshing LP cache')
    async def refresh(self, tokens):
        logger.debug(f'Refreshing LP cache for {len(tokens)} tokens ...')
        now = datetime.datetime.now()

        async def update(driver):
            (new_proxy, new_lp_ids) = \
                await self.refresh_driver(driver, tokens)
            old_proxy = self.lp_sync_proxies.get(driver.uid, None)
            if new_proxy is not None and old_proxy != new_proxy:
                new_proxy.subscribe_on_sync(self.on_sync)
                self.lp_sync_proxies[driver.uid] = new_proxy
                self.lp_sync_pool_ids[driver.uid] = new_lp_ids
                if old_proxy is not None:
                    old_proxy.unsubscribe_on_sync(self.on_sync)
                    await old_proxy.stop()            

        if len(tokens) > 0:
            await asyncio.gather(*[update(driver) for driver in self.lp_drivers])

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
    
    def on_sync(self, block: BlockId, proxy: LPSyncProxy):
        logger.debug(f'Proxy {proxy} synced to block {block.number}.')
        for uid, p in self.lp_sync_proxies.items():
            if p == proxy:
                self.driver_latest_block[uid] = block
                break
        if all(block == b for b in self.driver_latest_block.values()):
            async def f():
                await asyncio.sleep(0.01)  # yield current task
                logger.debug(f'Synced to new block {block.number}.')
            task = asyncio.create_task(f())
            self.background_tasks.add(task)
            task.add_done_callback(lambda _: self.background_tasks.remove(task))

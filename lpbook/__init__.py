import asyncio
from configparser import RawConfigParser
from copy import deepcopy
from enum import Enum
from itertools import groupby
import logging
from abc import ABC, abstractmethod
import os
from typing import Any, Dict, List

from lpbook.util import LP, Trade, traced
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.RecentEventLog import RecentEventLog
from lpbook.error import CacheMissError, TemporaryError
from lpbook.lp_monitors import lp_monitors
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

# if ethereum finality is 6 blocks,
# we would only need to keep 6 blocks since checkpoint.
MAX_NR_BLOCKS_TO_CHECKPOINT = int(os.getenv('MAX_NR_BLOCKS_TO_CHECKPOINT', 6))
START_BLOCK_LAG = max(MAX_NR_BLOCKS_TO_CHECKPOINT, int(os.getenv('START_BLOCK_LAG', MAX_NR_BLOCKS_TO_CHECKPOINT)))


class RecentStateCache:
    def __init__(self, cache_size):
        self.recent_block_hashes = []
        self.recent_block_numbers = []
        self.state_by_block_hash = {}
        self.cache_size = cache_size

    def get_block_hash(self, block_number: int) -> str:
        try:
            i = self.recent_block_numbers.index(block_number)
        except ValueError:
            raise CacheMissError(
                f'Could not find block {block_number} in recent state cache.'
            )
        return self.recent_block_hashes[i]

    def get_at_block_number(self, block_number: int) -> Any:
        return self.state_by_block_hash[self.get_block_hash(block_number)]

    def get_at_block_hash(self, block_hash: str) -> Any:
        try:
            return self.state_by_block_hash[block_hash]
        except KeyError:
            raise CacheMissError(
                f'Cound not find block {block_hash} in recent state cache.'
            )

    def get_at_block(self, block: BlockId) -> Any:
        """Returns the state at block if given, otherwise return most recently added."""
        if block.hash is not None:
            return self.get_at_block_hash(block.hash)
        elif block.number is not None:
            return self.get_at_block_number(block.number)
        return self.get_most_recently_added()

    def get_most_recently_added(self) -> Any:
        if len(self.recent_block_hashes) == 0:
            raise CacheMissError(
                f'Attempt to retrieve most recently added state from an empty {self}.'
            )
        return self.state_by_block_hash[self.recent_block_hashes[-1]]

    def add(self, block: BlockId, state) -> None:
        assert block.is_fully_qualified()
        self.recent_block_numbers.append(block.number)
        self.recent_block_hashes.append(block.hash)
        self.state_by_block_hash[block.hash] = state
        # Keep cache maximum size.
        if len(self.recent_block_numbers) > self.cache_size:
            assert len(self.recent_block_numbers) == self.cache_size + 1
            self.state_by_block_hash.pop(self.recent_block_hashes[0], None)
            self.recent_block_hashes = self.recent_block_hashes[1:]
            self.recent_block_numbers = self.recent_block_numbers[1:]


class LPAsyncProxy(ABC):
    """Asynchronous proxy to a collection of LP states indexed by block number/hash .

    Accessing states through this class usually implies a, possibly slow,
    call to the proxied data source.
    """
    @abstractmethod
    async def __call__(self, block: BlockId) -> Dict[str, LP]:
        """Returns a dictionary of LP states indexed by their LP id, at given block."""

    @abstractmethod
    async def latest_block(self) -> BlockId:
        """Returns the block of the latest state in the collection."""


class LPSyncProxy(ABC):
    """Synchronous proxy to a collection of LP states indexed by block number/hash.

    This proxy will be kept synchronized with the proxied data structure. Accessing state
    through this class will either be quick, or raise an error if the proxy is
    out of sync.
    """
    @abstractmethod
    def __call__(self, block: BlockId) -> Dict[str, LP]:
        """Returns the recent state if synced, or an error otherwise."""

    @abstractmethod
    async def start(self) -> None:
        """Starts syncing proxy with proxied data source."""

    @abstractmethod
    async def stop(self) -> None:
        """Stops syncing proxy with proxied data source."""


class LPSyncProxyFromAsyncProxy(LPSyncProxy):
    """Generic adaptor to provide a LPSyncProxy from a LPAsyncProxy.

    Default implementation that simply queries and caches underlying LPSyncProxy at
    every block.
    """

    CACHE_SIZE = 25

    def __init__(
        self,
        underlying_lp_async_proxy: LPAsyncProxy,
        block_stream: BlockStream
    ):
        self.recent_state_cache = RecentStateCache(self.CACHE_SIZE)
        self.underlying_lp_async_proxy = underlying_lp_async_proxy
        self.block_stream = block_stream
        self.block_stream.subscribe(self.query_underlying_lp_async_proxy)

    async def __del__(self):
        self.block_stream.unsubscribe(self.query_underlying_lp_async_proxy)

    async def query_underlying_lp_async_proxy(
        self,
        block: BlockId
    ):
        # Try hard to keep it in sync.
        while True:
            try:
                state = await self.underlying_lp_async_proxy(block)
                break
            except TemporaryError as err:
                logger.warning(
                    f'Could not obtain state for block {block} from '
                    f'underlying lp async proxy:\n\t{err}\n\tRetrying in 5 seconds ...'
                )
                await asyncio.sleep(5)

            except Exception as err:
                logger.error(
                    f'Could not obtain state for block {block} from '
                    f'underlying lp async proxy:\n\t{err}\n\t'
                    'Exiting since data is now potentially inconsistent.'
                )
                raise

        self.recent_state_cache.add(block=block, state=state)

    def __call__(self, block: BlockId) -> Dict[str, LP]:
        """Returns the required state if cached, or raise a CacheMissError otherwise."""
        return self.recent_state_cache.get_at_block(block)

    async def start(self) -> None:
        pass

    async def stop(self) -> None:
        self.block_stream.unsubscribe(self.query_underlying_lp_async_proxy)


class LPFromInitialStatePlusChangesProxy(LPSyncProxy):
    def __init__(self, contracts, events, async_proxy, event_stream, web3_client, extra_topics=tuple()):
        self.contracts = contracts
        self.events = events
        self.async_proxy = async_proxy
        self.web3_client = web3_client
        self.event_stream = event_stream
        self.extra_topics = extra_topics
        self.event_log = RecentEventLog(web3_client, event_stream)
        self.checkpoint = None
        self.latest_block_number_by_lp_id = {}
        self.extra_event_updaters_by_event = {}
        self.create_extra_updaters_tasks = set()
        self.running = False

    def __del__(self):        
        for task in self.create_extra_updaters_tasks:
            task.cancel()

    @traced(logger, 'Resetting LPFromInitialStatePlusChangesProxy')
    async def reset_event_log(self, reason: RuntimeError) -> None:
        await self.stop()
        self.event_log = RecentEventLog(
            self.web3_client, self.event_stream
        )
        self.checkpoint = None
        self.start()

    @traced(logger, 'Starting LPFromInitialStatePlusChangesProxy')
    async def start(self) -> None:
        self.running = True
        self.event_log.subscribe(self.on_new_events)
        # since async_proxy might not be up to date,
        # it is what defines the start block.
        latest_block = await self.async_proxy.latest_block()
        start_block_number = latest_block.number - START_BLOCK_LAG
        b = await self.web3_client.eth.get_block(start_block_number)
        start_block_hash = b.hash
        start_block = BlockId(number=start_block_number, hash=start_block_hash, timestamp=b.timestamp)
        self.checkpoint = await self.async_proxy(start_block)

        # FIXME: this really shouldn't be here...
        if lp_monitors is not None:
            for lp in self.checkpoint.values():
                lp_monitors.initialize(lp, start_block.number)

        await self.event_log.start(
            self.contracts,
            self.events,
            start_block.number + 1,  # Because checkpoint is at the end of start_block
            self.reset_event_log,
            extra_topics=self.extra_topics
        )

    @traced(logger, 'Stopping LPFromInitialStatePlusChangesProxy')
    async def stop(self) -> None:
        if not self.running:
            return
        self.event_log.unsubscribe(self.on_new_events)
        await self.event_log.stop()
        self.running = False

    def __call__(self, block: BlockId) -> Dict[str, LP]:
        """Returns a list of lps with state at (the end of) given block.

        If block is specified, then return lps state at that block if possible,
        otherwise will raise a CacheMissError.
        """

        logger.debug(f'Querying {self} (block={block}) ...')

        events_since_checkpoint = self.event_log(block)

        state = self.get_state(self.checkpoint, events_since_checkpoint)

        # FIXME: this really shouldn't be here...
        if lp_monitors is not None:
            trades = self.get_trades(self.checkpoint, events_since_checkpoint)
            # For monitoring purposes, it is fine if reorgs are not taken into account.
            trades = [trade for trade in trades if trade.block_number > self.latest_block_number_by_lp_id.get(trade.lp_id, 0)]
            for trade in trades:
                lp_monitors.record_trade(trade)
                self.latest_block_number_by_lp_id[trade.lp_id] = trade.block_number

        self.update_checkpoint()

        for lp in state.values():
            lp.block = block 

        logger.debug(f'Querying {self} (block={block}) ... done')

        return state

    def update_checkpoint(self):
        # Update checkpoint to computed state to save extra computation and memory on
        # future calls.
        if self.event_log.block_count <= MAX_NR_BLOCKS_TO_CHECKPOINT:
            return
        logger.debug('Updating checkpoint.')
        nr_blocks_to_free = self.event_log.block_count - \
            MAX_NR_BLOCKS_TO_CHECKPOINT
        min_start_block_number = self.event_log.start_block_number + nr_blocks_to_free
        min_start_block = BlockId(number=min_start_block_number - 1)
        events_since_checkpoint = self.event_log(min_start_block)                
        self.checkpoint = self.get_state(self.checkpoint, events_since_checkpoint)
        for event in events_since_checkpoint:
            self.extra_event_updaters_by_event.pop(event, None)
        self.event_log.update_start_block(min_start_block_number)

    def get_state(self, prev_state, events_since_checkpoint) -> Dict[str, LP]:
        """Assembles state from checkpoint and delta."""
        state = deepcopy(prev_state)
        for event in events_since_checkpoint:
            self.update_state(state, event)
            for extra_updater in self.extra_event_updaters_by_event.get(event, []):
                extra_updater(state)
        return state
    
    def create_extra_event_updaters(self, events, create_extra_updater_async_fn, name):     
        @traced(logger, f"Running extra updater for '{name}'")   
        async def helper():
            updaters = await asyncio.gather(*[create_extra_updater_async_fn(event) for event in events])
            for updater, event in zip(updaters, events):
                if updater is not None:
                    self.extra_event_updaters_by_event.setdefault(event, []).append(updater)
        create_extra_updaters_task = asyncio.create_task(helper())
        create_extra_updaters_task.add_done_callback(lambda _: self.create_extra_updaters_tasks.remove(create_extra_updaters_task))
        self.create_extra_updaters_tasks.add(create_extra_updaters_task)

    @abstractmethod
    def update_state(self, state, event) -> None:
        """Updates state with event."""

    def get_trades(self, cur_state: Dict[str, LP], delta) -> list[Trade]:
        """Assembles trades from checkpoint and delta."""
        return []

    def on_new_events(self, events) -> None:
        """Callback for new events."""


# Creates an LPSyncProxy from an aggregation of LPFromInitialStatePlusChangesProxy,
# interpolating events as necessary. This allows to create async proxies to LPs whose
# state must be updated by events from multiple contracts.
class MultiLPFromInitialStatePlusChangesProxy(LPSyncProxy):
    def __init__(self, proxies: List[LPFromInitialStatePlusChangesProxy]):
        self.proxies = proxies
        self.checkpoint = None

    @traced(logger, 'Starting MultiLPFromInitialStatePlusChangesProxy')
    async def start(self) -> None:
        await asyncio.gather(*[p.start() for p in self.proxies])

    @traced(logger, 'Stopping MultiLPFromInitialStatePlusChangesProxy')
    async def stop(self) -> None:
        for p in self.proxies:
            await p.stop()

    def __call__(self, block: BlockId) -> Dict[str, LP]:
        """Returns a list of lps with state at (the end of) given block.

        If block is specified, then return lps state at that block if possible,
        otherwise will raise a CacheMissError.
        """

        logger.debug(f'Querying {self} (block={block}) ...')

        if self.checkpoint is None:
            # All proxies must have the same checkpoint.
            for i in range(1, len(self.proxies)):
                assert self.proxies[i].checkpoint == self.proxies[0].checkpoint
            self.checkpoint = self.proxies[0].checkpoint

        # slice events by proxy
        events_since_checkpoint = self.collect_events_since_checkpoint(block)

        state = self.get_state(self.checkpoint, events_since_checkpoint)

        self.update_checkpoint()

        for lp in state.values():
            lp.block = block 

        logger.debug(f'Querying {self} (block={block}) ... done')

        return state
    
    def collect_events_since_checkpoint(self, block):
        events_since_checkpoint = [(proxy, event) for proxy in self.proxies for event in proxy.event_log(block)]
        events_since_checkpoint = sorted(events_since_checkpoint, key=lambda pe: (not pe[1].removed, pe[1].blockNumber, pe[1].logIndex))
        events_since_checkpoint = [(p, [pe[1] for pe in events]) for p, events in groupby(events_since_checkpoint, lambda pe: pe[0])]
        return events_since_checkpoint

    def update_checkpoint(self):
        # Update checkpoint to computed state to save extra computation and memory on
        # future calls.
        max_block_count = max(proxy.event_log.block_count for proxy in self.proxies)
        if max_block_count <= MAX_NR_BLOCKS_TO_CHECKPOINT:
            return
        logger.debug('Updating checkpoint.')
        nr_blocks_to_free = max_block_count - MAX_NR_BLOCKS_TO_CHECKPOINT
        min_start_block_number = min(proxy.event_log.start_block_number for proxy in self.proxies) + nr_blocks_to_free
        min_start_block = BlockId(number=min_start_block_number - 1)
        events_since_checkpoint = self.collect_events_since_checkpoint(min_start_block)
        self.checkpoint = self.get_state(self.checkpoint, events_since_checkpoint)
        for proxy in self.proxies:
            proxy.checkpoint = self.checkpoint
            proxy.event_log.update_start_block(min_start_block_number)

    def get_state(self, checkpoint, events_since_checkpoint) -> Dict[str, LP]:
        """Assembles state from checkpoint and delta."""
        state = checkpoint
        for proxy, events in events_since_checkpoint:
            state = proxy.get_state(state, events)
        return state

class LPDriver(ABC):
    class LPSyncProxyDataSource(Enum):
        Default = 0
        TheGraph = 1
        Web3 = 2
        TheGraphAndWeb3 = 3

    class LPAsyncProxyDataSource(Enum):
        Default = 0
        TheGraph = 1
        Web3 = 2

    def __init__(self, lp_cls):
        self.lp_cls = lp_cls

    @property
    def protocol_name(self) -> str:
        """Returns unique identifier for lp protocol."""
        return self.lp_cls.protocol_name

    @property
    def protocol_version(self) -> str:
        """Returns unique identifier for lp protocol version."""
        return self.lp_cls.protocol_version

    @property
    def protocol(self) -> str:
        """Returns unique identifier for lp protocol and version."""
        return f'{self.protocol_name}_{self.protocol_version}'

    @property
    def kind(self) -> str:
        """Returns the api of the state."""
        return self.lp_cls.kind

    @property
    def uid(self) -> str:
        """Returns the kind and protocol of the lp."""
        return f'{self.protocol}_{self.kind}'

    @abstractmethod
    async def create_lp_sync_proxy(self, lp_ids: List[str]) -> LPSyncProxy:
        """Creates a new LPSyncProxy instance that tracks a set of lps."""

    @abstractmethod
    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        """Collects addresses of lps involving given tokens."""

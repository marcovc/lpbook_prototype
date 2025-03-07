from abc import abstractmethod
import asyncio
import logging
from typing import Optional
from web3 import AsyncWeb3
from web3.providers.persistent import (
    WebSocketProvider,
)

from lpbook.util import traced
from lpbook.web3 import BlockId

logger = logging.getLogger(__name__)


class BlockScanning:
    """A set of methods that need to exist on any streams/proxies scanning blocks."""

    @property
    @abstractmethod
    def last_block(self) -> Optional[BlockId]:
        """Most recent block scanned, or none if no blocks were scanned.

        The block must be fully qualified.
        """


class BlockStream(BlockScanning):
    """Maintains a table of block number/hashes from a given block onwards."""

    # The "delay" parameter allows to specify a small delay before advertising new block. This
    # is useful since a node is typically not consistent, e.g. it can advertise
    # a new block, but then an immediate call for the logs might not return
    # the most recent results.
    def __init__(self, web3_ws, delay: float=0):
        """web3_ws should be a node websocket endpoint"""
        self.web3_ws = web3_ws
        self.subscribers = []
        #self._last_block = None
        self._last_block_number = None
        self._last_block_hash = None
        self._last_block_timestamp = None
        self.running = False
        self.delay = delay
        self.on_first_block = asyncio.Event()

    @property
    def last_block(self) -> Optional[BlockId]:
        #return self._last_block
        return BlockId(number=self._last_block_number, hash=self._last_block_hash, timestamp=self._last_block_timestamp)

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            return
        self.subscribers = [s for s in self.subscribers if s != subscriber]

    async def trigger(self, block: BlockId):
        assert block.is_fully_qualified()
        prev_last_block_number = self._last_block_number
        self._last_block_number = block.number
        self._last_block_hash = block.hash
        self._last_block_timestamp = block.timestamp
        if prev_last_block_number is None:
            self.on_first_block.set()
        await asyncio.gather(
            *[
                subscriber(block)
                for subscriber in self.subscribers
            ]
        )

    async def run_helper(self, w3, start_block_number: int = None):
        """Listens for new blocks and calls subscribers on each of them.

        If start_block_number is not None, then it will first call subscribers
        on each block in [start_block_number, current_block_number[.
        """
        if start_block_number is not None:
            while self.running:
                latest_block_number = await w3.eth.get_block_number()
                if start_block_number > latest_block_number:
                    await asyncio.sleep(15)
                    continue
                assert start_block_number <= latest_block_number
                start_block = await w3.eth.get_block(start_block_number)
                if self.delay > 0:
                    await asyncio.sleep(self.delay)
                logger.debug(
                    f'Telling subscribers about past block {start_block_number}'
                    f'/{start_block.hash.hex()[:8]}'
                )
                await self.trigger(BlockId.from_web3(start_block))
                if start_block_number == latest_block_number:
                    break
                start_block_number += 1

            if not self.running:
                return

        logger.debug('Finished processing past blocks')

        subscription_id = await w3.eth.subscribe('newHeads')
        async for message in w3.socket.process_subscriptions():

            # TODO: How to validate that subscription was correct?
            #assert 'id' in json.loads(subscription_response).keys()
            
            if not self.running:
                break

            message = message["result"]
            #message = await ws.recv()
            #message = json.loads(message)
            block_number = message.number
            assert start_block_number is None or block_number >= start_block_number
            # this avoids a notifying twice about the same block, which can happen
            # when "stitching" the processing of past blocks above with this loop.
            if start_block_number is not None and block_number == start_block_number:
                continue
            block_hash = message.hash
            logger.debug(
                f'Detected new block {block_number}/{block_hash.hex()[:8]}. '
                'Telling subscribers about it ...'
            )
            timestamp = message.timestamp
            await self.trigger(BlockId(number=block_number, hash=block_hash, timestamp=timestamp))

    @traced(logger, 'Running BlockStream')
    async def run(self, start_block_number: int = None):
        """Listens for new blocks and calls subscribers on each of them.

        If start_block_number is not None, then it will first call subscribers
        on each block in [start_block_number, current_block_number[
        """
        self.running = True
        async for w3 in AsyncWeb3(WebSocketProvider(self.web3_ws)):
            await self.run_helper(w3, start_block_number)
            if not self.running:
                break

    def shutdown(self):
        self.running = False

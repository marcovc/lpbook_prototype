from abc import abstractproperty
import asyncio
import datetime
import json
import logging
from socket import gaierror
from typing import Optional
from requests import ReadTimeout
from web3 import Web3

from websockets import connect
from websockets.exceptions import ConnectionClosedError

from lpbook.util import traced
from lpbook.web3 import BlockId

logger = logging.getLogger(__name__)


class BlockScanning:
    """A set of methods that need to exist on any streams/proxies scanning blocks."""

    @abstractproperty
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
        self._last_block_number = block.number
        self._last_block_hash = block.hash
        self._last_block_timestamp = block.timestamp
        await asyncio.gather(
            *[
                subscriber(block)
                for subscriber in self.subscribers
            ]
        )

    async def run_helper(self, start_block_number: int = None):
        """Listens for new blocks and calls subscribers on each of them.

        If start_block_number is not None, then it will first call subscribers
        on each block in [start_block_number, current_block_number[.
        """
        self.running = True
        if start_block_number is not None:
            w3 = Web3(Web3.WebsocketProvider(self.web3_ws))
            while self.running:
                latest_block_number = w3.eth.get_block_number()
                if start_block_number > latest_block_number:
                    await asyncio.sleep(15)
                    continue
                assert start_block_number <= latest_block_number
                start_block = w3.eth.get_block(start_block_number)
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

        logger.debug(f'{self} has finished processing past blocks')
        async with connect(self.web3_ws) as ws:
            await ws.send(json.dumps({
                'id': 1,
                'method': 'eth_subscribe',
                'params': ['newHeads'],
                'jsonrpc': '2.0'
            }))
            subscription_response = await ws.recv()

            # TODO: How to validate that subscription was correct?
            assert 'id' in json.loads(subscription_response).keys()
            
            while self.running:
                message = await ws.recv()
                message = json.loads(message)
                block_number = int(message['params']['result']['number'], base=16)
                assert start_block_number is None or block_number >= start_block_number
                # this avoids a notifying twice about the same block, which can happen
                # when "stitching" the processing of past blocks above with this loop.
                if start_block_number is not None and block_number == start_block_number:
                    continue
                block_hash = message['params']['result']['hash']
                logger.debug(
                    f'Detected new block {block_number}/{block_hash[:8]}. '
                    'Telling subscribers about it ...'
                )
                timestamp = int(message['params']['result']['timestamp'], 16)
                await self.trigger(BlockId(number=block_number, hash=block_hash, timestamp=timestamp))

    @traced(logger, 'Running BlockStream')
    async def run(self, start_block_number: int = None):
        """Listens for new blocks and calls subscribers on each of them.

        If start_block_number is not None, then it will first call subscribers
        on each block in [start_block_number, current_block_number[
        """
        await self.run_helper(start_block_number)

    def shutdown(self):
        self.running = False

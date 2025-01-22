

import asyncio
import datetime
import logging
from typing import List
from fastapi import WebSocket

from lpbook.LPCache import LPCache
from lpbook.execution import LPStats
from lpbook.server.ProcessServer import ProcessServer
from lpbook.server.util import create_lps_response, create_order_lps_response
from lpbook.util import LP
from lpbook.web3 import BlockId

logger = logging.getLogger(__name__)

# TEMP:
import psutil

# To use all the avaiable machinery in place for standard http requests, i.e. the ProcessServer,
# this class keeps its own cache of token ids, and queries the ProcessServer for all lps
# involving those tokens at each block.
class WebsocketDriver:
    POOL_MAX_UNUSED_AGE: datetime.timedelta = LPCache.POOL_MAX_UNUSED_AGE
    POOL_MAX_CACHE_SIZE: int = LPCache.POOL_MAX_CACHE_SIZE

    def __init__(self, lp_stats: LPStats, process_server: ProcessServer):
        self.lp_stats = lp_stats
        self.process_server = process_server
        self.active_connections: List[WebSocket] = []
        self.requested_token_ids = {}
        self.latest_cache_prune_time = datetime.datetime.now()
        self.nr_requests_for_cached_tokens = 0
        self.total_nr_requests = 0

    def update_token_ids(self, token_ids: List[str]):
        now = datetime.datetime.now()
        for token_id in token_ids:
            self.nr_requests_for_cached_tokens += int(token_id in self.process_server.lp_cache.cached_tokens)
            self.total_nr_requests += 1
            self.requested_token_ids[token_id] = now
        

    def print_system_stats(self):
        logger.debug(
            f"Tokens: {len(self.requested_token_ids)}, Cache hit: {self.nr_requests_for_cached_tokens / (self.total_nr_requests + 1) * 100:.2f}%, "
            f"CPU: {psutil.cpu_percent()}%, Memory: {psutil.virtual_memory().percent}%, "
            f"Threads: {psutil.Process().num_threads()}, Tasks: {len(asyncio.all_tasks())}, "
            f"Connections: {len(self.active_connections)}")

    async def run(self):
        logger.debug("Starting ...")
        while True:
            try:
                # We need a timeout because process server may be restarted (e.g. due to an exception), in which case we would
                # be waiting indefinitely.
                block = await asyncio.wait_for(self.process_server.wait_for_block(), 20)
                await asyncio.sleep(1.5)   # give a chance for events to propagate
                lps = await self.process_server.get_lps_trading_tokens(set(self.requested_token_ids.keys()), block_number=block.number)
                order_lps = self.process_server.get_order_lps(block_number=block.number)
                await self.broadcast(lps, order_lps, block)
                self.prune_cache()
                self.print_system_stats()
            except asyncio.TimeoutError:
                logger.warning("Timeout waiting for block. Continuing ...")
            except Exception:
                logger.exception("Unhandled exception. Continuing ...")

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except ValueError:
            pass

    async def disconnect_all(self):
        for websocket in self.active_connections:
            await websocket.close()
        self.active_connections = []

    async def broadcast(self, lps: List[LP], order_lps: List[LP], block: BlockId):
        lps_j = create_lps_response(lps, block.number, block.hash, block.timestamp, False, self.lp_stats, self.process_server)
        order_lps_j = create_order_lps_response(order_lps, block) 

        # Timeout is needed to exit possible deadlock between client and server.
        async def send_reply_with_timeout(connection):
            try:
                await asyncio.wait_for(connection.send_json({"lps": lps_j, "order_lps": order_lps_j}), timeout=10)
            except asyncio.TimeoutError:
                logger.warning("Timeout sending data to client. Disconnecting ...")
                self.disconnect(connection)
                await connection.close()

        await asyncio.gather(*[
            send_reply_with_timeout(connection)
            for connection in self.active_connections
        ])

    def prune_cache(self):
        if len(self.requested_token_ids) > self.POOL_MAX_CACHE_SIZE:
            self.prune_cache_by_size()
        if datetime.datetime.now() - self.latest_cache_prune_time > self.POOL_MAX_UNUSED_AGE:
            self.prune_cache_by_age()

    def prune_cache_by_size(self):
        # To avoid prunning every time, we prune to 90% of the max size.
        self.requested_token_ids = {
            token_id: time
            for token_id, time in sorted(self.requested_token_ids.items(), key=lambda x: x[1])[:int(self.POOL_MAX_CACHE_SIZE * 0.9)]
        }

    def prune_cache_by_age(self):
        now = datetime.datetime.now()
        if now - self.latest_cache_prune_time <= self.POOL_MAX_UNUSED_AGE:
            return
        self.requested_token_ids = {
            token_id: time
            for token_id, time in self.requested_token_ids.items()
            if now - time <= self.POOL_MAX_UNUSED_AGE
        }
        self.latest_cache_prune_time = now

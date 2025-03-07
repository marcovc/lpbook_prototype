

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

class WebsocketDriver:

    def __init__(self, lp_stats: LPStats, process_server: ProcessServer):
        self.lp_stats = lp_stats
        self.process_server = process_server
        self.active_connections: List[WebSocket] = []      

    def stats_report(self):
        return {"Connections": len(self.active_connections)}

    async def run_once(self, block: BlockId):
        try:
            lps = await self.process_server.get_lps_trading_tokens(self.process_server.lp_cache.cached_tokens, block_number=block.number)
            order_lps = self.process_server.get_order_lps(block_number=block.number)
            await self.broadcast(lps, order_lps, block)
        except Exception:
            logger.exception("Unhandled exception. Continuing ...")

    async def run(self):
        logger.debug("Starting ...")
        while True:
            try:
                # We need a timeout because process server may be restarted (e.g. due to an exception), in which case we would
                # be waiting indefinitely.
                block = await asyncio.wait_for(self.process_server.wait_for_block(), 20)
                await asyncio.sleep(1.5)   # give a chance for events to propagate
                await self.run_once(block)
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
        lps_j = create_lps_response(lps, block.number, block.hash, block.timestamp, self.lp_stats, self.process_server.lp_cache)
        order_lps_j = create_order_lps_response(order_lps, block) 
        response = {
            "lps": lps_j,
            "order_lps": order_lps_j,
            "prev_block_number": block.number,
            "prev_block_hash": block.hash.to_0x_hex(),
            "prev_block_timestamp": block.timestamp,
        }
        # Timeout is needed to exit possible deadlock between client and server.
        async def send_reply_with_timeout(connection):
            try:
                await asyncio.wait_for(connection.send_json(response), timeout=10)
            except asyncio.TimeoutError:
                logger.warning("Timeout sending data to client. Disconnecting ...")
                self.disconnect(connection)
                await connection.close()

        await asyncio.gather(*[
            send_reply_with_timeout(connection)
            for connection in self.active_connections
        ])


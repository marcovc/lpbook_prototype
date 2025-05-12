

import asyncio
import datetime
import logging
import os
from typing import List, Optional, Tuple
from fastapi import WebSocket

from lpbook.lp_monitors import lp_monitors
from lpbook.server.util import create_lps_response, create_order_lps_response
from lpbook.util import LP, Token
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream

logger = logging.getLogger(__name__)

WS_WEB3_URL = os.getenv('WS_WEB3_URL')

class PriceWebsocketDriver:

    def __init__(self):
        self.active_connections: List[WebSocket] = []      
        self.block_stream = BlockStream(WS_WEB3_URL, 0)

    def __del__(self):
        self.shutdown()

    def stats_report(self):
        return {"Connections": len(self.active_connections)}

    async def run_once(self):
        if lp_monitors is None:
            return            
        block = self.block_stream.last_block
        assert block is not None
        all_token_pairs = lp_monitors.traded_amount_collectors.token_pairs
        token_pairs_quoted_in_native_token = {
            (token1, token2)
            for token1, token2 in all_token_pairs
            if token2.is_wrapped_native_token()
        }
        if len(token_pairs_quoted_in_native_token) == 0:
            logger.debug("No prices to report.")
            return 

        direct_estimates = lp_monitors.traded_amount_collectors.estimate_average_xrates_in_running_hour(
            token_pairs_quoted_in_native_token, 
            block.number, 
            block.datetime()
        )
        
        # TODO: indirect estimates ?

        wrapped_native_token = list(token_pairs_quoted_in_native_token)[0][1]
        prices = {
            k[0]: v for k, v in direct_estimates.items()
        } | {
            wrapped_native_token: (1, 0),
            Token.native_token_as_erc20(): (1, 0)
        }

        await self.broadcast(prices)

    async def run(self):
        logger.debug("Starting ...")
        self.running = True
        fetch_block_task = asyncio.create_task(self.block_stream.run())
        await self.block_stream.on_first_block.wait()
        while self.running:
            try:
                await self.run_once()
                await asyncio.sleep(60)
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

    async def broadcast(self, prices: dict[Token, Tuple[float, Optional[float]]]):        
        # Timeout is needed to exit possible deadlock between client and server.
        
        async def send_reply_with_timeout(connection):
            try:
                await asyncio.wait_for(connection.send_json({k.address: v for k, v in prices.items()}), timeout=10)
            except asyncio.TimeoutError:
                logger.warning("Timeout sending data to client. Disconnecting ...")
                self.disconnect(connection)
                await connection.close()

        await asyncio.gather(*[
            send_reply_with_timeout(connection)
            for connection in self.active_connections
        ])

    def shutdown(self):
        self.block_stream.shutdown()
        self.running = False

    """
    def collect_indirect_estimates(self):
        all_token_pairs = lp_monitors.traded_amount_collectors.token_pairs
        all_tokens = {token for token1, token2 in all_token_pairs for token in (token1, token2)}  
        tokens_with_direct_estimates = {
            token1
            for token1, token2 in all_token_pairs
            if token2.is_wrapped_native_token()
        }
        #tokens_without_direct_estimates = all_tokens - tokens_with_direct_estimates
    """
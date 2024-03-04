import asyncio
import logging
import os
import sys
import traceback
from typing import List, Optional

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
from lpbook.LPCache import LPCache
from lpbook.LPHistoric import LPHistoric
from lpbook.lps.curve import CurveDriver
from lpbook.lps.uniswap_v3 import UniV3Driver, PancakeswapV3Driver
from lpbook.lps.uniswap_v2 import SushiDriver, UniV2Driver, PancakeswapV2Driver
from lpbook.lps.maker_psm import MakerPSMDriver
from lpbook.lps.piecewise import NativeDriver, HashflowDriver
from lpbook.lps.balancer_v2 import BalancerV2Driver
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import ServerFilteredEventStream
from pydantic_settings import BaseSettings
from web3 import Web3
import aioprocessing

from lpbook.util import LP

logger = logging.getLogger(__name__)

class ProcessServer:
    def __init__(self, protocols, profiling):
        self.protocols = protocols
        self.profiling = profiling

    async def reset(self):
        logger.info("Resetting LPBook ...")

        HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
        WS_WEB3_URL = os.getenv('WS_WEB3_URL')

        import requests
        requests_adapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)
        requests_session = requests.Session()
        requests_session.mount('http://', requests_adapter)
        requests_session.mount('https://', requests_adapter)
        w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL, session=requests_session))

        self.block_stream = BlockStream(WS_WEB3_URL)
        event_stream = ServerFilteredEventStream(self.block_stream, w3)
        self.aiohttp_session = aiohttp.ClientSession()

        drivers = []

        # LP drivers
        if "univ3" in self.protocols:
            drivers.append(UniV3Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "pancakeswapv3" in self.protocols:
            drivers.append(PancakeswapV3Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "curve" in self.protocols:
            drivers.append(CurveDriver(self.block_stream, self.aiohttp_session, w3))
        if "univ2" in self.protocols:
            drivers.append(UniV2Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "sushi" in self.protocols:
            drivers.append(SushiDriver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "pancakeswapv2" in self.protocols:
            drivers.append(PancakeswapV2Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "makerpsm" in self.protocols:
            drivers.append(MakerPSMDriver())
        if "native" in self.protocols:
            drivers.append(NativeDriver(self.aiohttp_session))
        if "hashflow" in self.protocols:
            drivers.append(HashflowDriver(self.aiohttp_session))
        if "balancerv2" in self.protocols:
            drivers.append(BalancerV2Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        for driver in drivers:
            logger.info(f"Enabled driver {driver.__class__.__name__}.")

        # Create LP Cache (main service)
        # Returns current state (fast).
        
        self.lp_cache = LPCache(drivers)

        # Create LP Historic (main service)
        # Returns past state (slow).
        # self.lp_historic = LPHistoric([univ3_driver, sushi_driver, curve_driver])

        await asyncio.gather(
            self.block_stream.run(),
            self.lp_cache.run()
        )

    @property
    def last_block(self) -> Optional[BlockId]:
        return self.block_stream.last_block
    
    def start(self):
        async def run_loop():
            self.running = True
            while self.running:
                try:
                    await self.reset()
                except Exception as e:
                    logger.error(
                        f"Received unhandled exception: {str(e)}. Resetting."
                        f"Traceback:\n{traceback.format_exc()}\n"
                    )
        self.runloop_task = asyncio.create_task(run_loop())

    async def shutdown(self):
        self.running = False
        self.block_stream.shutdown()
        self.lp_cache.shutdown()
        await self.aiohttp_session.close()

    def get_lps_trading_tokens(self, token_ids: set, block_number=None) -> List[LP]:
        return self.lp_cache.get_lps_trading_tokens(token_ids, block_number)
    

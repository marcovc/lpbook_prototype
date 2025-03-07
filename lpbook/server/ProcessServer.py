import asyncio
import datetime
import logging
import os
import sys
import traceback
from typing import List, Optional, Set, Tuple

import aiohttp
import psutil
from lpbook.lps.cowamm import COWAMMBalancerDriver, COWAMMPrivateDriver
from lpbook.lps.fixedrate import StaticFixedRateDriver
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
from lpbook.LPCache import LPCache
from lpbook.LPHistoric import LPHistoric
from lpbook.lps.curve import CurveDriver, CurveNGDriver
from lpbook.lps.fixedrate.susds import SUDSDDriver
from lpbook.lps.fluid import FluidDriver
from lpbook.lps.uniswap_v3 import SolidlyV3Driver, UniV3Driver, PancakeswapV3Driver
from lpbook.lps.uniswap_v2 import SushiDriver, SwaprV2Driver, UniV2Driver, PancakeswapV2Driver
from lpbook.lps.piecewise import BebopDriver, NativeDriver, HashflowDriver, ZeroExDriver
from lpbook.lps.balancer_v2 import BalancerV2WeightedDriver, BalancerV2StableDriver
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import ServerFilteredEventStream
from pydantic_settings import BaseSettings
from web3 import AsyncWeb3, AsyncIPCProvider
from lpbook.web3.TokenDB import TokenDB
import aioprocessing

from lpbook.util import LP, Token

logger = logging.getLogger(__name__)

HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
WS_WEB3_URL = os.getenv('WS_WEB3_URL')
IPC_WEB3_URL = os.getenv('IPC_WEB3_URL')

class ProcessServer:
    def __init__(self, protocols, mandatory_amms: dict[str, set[str]], state_directory: str, profiling):
        self.protocols = protocols
        self.mandatory_amms = mandatory_amms
        self.state_directory = state_directory
        self.profiling = profiling
        self.on_reset_subscribers = []
        self.on_sync_subscribers = []

    def subscribe_on_reset(self, subscriber):
        self.on_reset_subscribers.append(subscriber)

    def subscribe_on_sync(self, subscriber):
        self.on_sync_subscribers.append(subscriber)

    async def reset(self):
        logger.info("Resetting LPBook ...")

        logger.info(f"Config:\n\tHTTP_WEB3_URL={HTTP_WEB3_URL}\n\tWS_WEB3_URL={WS_WEB3_URL}")

        #w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL, session=requests_session))
        w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(HTTP_WEB3_URL))
        #w3 = AsyncWeb3(AsyncWeb3.WebSocketProvider(WS_WEB3_URL))

        self.block_stream = BlockStream(WS_WEB3_URL, 0.1)   # pause 0.1 seconds before announcing new blocks to subscribers
        event_stream = ServerFilteredEventStream(self.block_stream, w3)
        self.aiohttp_session = aiohttp.ClientSession()

        self.token_db = TokenDB(w3, self.state_directory)

        lp_drivers = []
        order_drivers = []

        # LP drivers
        if "univ3" in self.protocols:
            lp_drivers.append(UniV3Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "pancakeswapv3" in self.protocols:
            lp_drivers.append(PancakeswapV3Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "solidlyv3" in self.protocols:
            lp_drivers.append(SolidlyV3Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "curve" in self.protocols:
            lp_drivers.append(CurveDriver(event_stream, self.aiohttp_session, w3))
        if "curveng" in self.protocols:
            lp_drivers.append(CurveNGDriver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "univ2" in self.protocols:
            lp_drivers.append(UniV2Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "sushi" in self.protocols:
            lp_drivers.append(SushiDriver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "pancakeswapv2" in self.protocols:
            lp_drivers.append(PancakeswapV2Driver(event_stream, self.block_stream, self.aiohttp_session, w3))
        if "swaprv2" in self.protocols:
            lp_drivers.append(SwaprV2Driver(event_stream, self.block_stream, self.aiohttp_session, w3))        
        if "fixedrate" in self.protocols:
            lp_drivers.append(StaticFixedRateDriver(self.block_stream))
        if "susds" in self.protocols:
            lp_drivers.append(SUDSDDriver(event_stream, w3))
        if "native" in self.protocols:
            lp_drivers.append(NativeDriver(self.aiohttp_session))
        if "hashflow" in self.protocols:
            lp_drivers.append(HashflowDriver())
        if "zeroex" in self.protocols:
            lp_drivers.append(ZeroExDriver(self.token_db))
        if "balancerv2weighted" in self.protocols:
            lp_drivers.append(BalancerV2WeightedDriver(self.token_db, event_stream, self.block_stream, self.aiohttp_session, w3))
        if "balancerv2stable" in self.protocols:
            lp_drivers.append(BalancerV2StableDriver(self.token_db, event_stream, self.block_stream, self.aiohttp_session, w3))
        if "bebop" in self.protocols:
            lp_drivers.append(BebopDriver(self.token_db))
        if "fluid" in self.protocols:
            lp_drivers.append(FluidDriver(self.block_stream, self.token_db, w3))
        if "cowammbalancer" in self.protocols:
            order_drivers.append(COWAMMBalancerDriver(event_stream, self.block_stream, self.token_db, w3))
        if "cowammprivate" in self.protocols:
            order_drivers.append(COWAMMPrivateDriver(event_stream, self.token_db, w3))
        for driver in lp_drivers:
            logger.info(f"Enabled LP driver {driver.__class__.__name__}.")
        for driver in order_drivers:
            logger.info(f"Enabled order driver {driver.__class__.__name__}.")

        # Create LP Cache (main service)
        # Returns current state (fast).
        
        self.lp_cache = LPCache(lp_drivers, order_drivers, self.block_stream, self.state_directory, self.mandatory_amms)

        for subscriber in self.on_sync_subscribers:
            self.lp_cache.subscribe_on_sync(subscriber)

        # Create LP Historic (main service)
        # Returns past state (slow).
        # self.lp_historic = LPHistoric([univ3_driver, sushi_driver, curve_driver])

        for subscriber in self.on_reset_subscribers:
            await subscriber()

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
                        f"Received unhandled exception: {str(e)}."
                        f"Traceback:\n{traceback.format_exc()}\n"
                    )                    
                    await self.shutdown()
                    self.running = True

        self.runloop_task = asyncio.create_task(run_loop())
        self.runloop_task.add_done_callback(lambda _: logger.debug("Run loop has exited."))
        self.stats_report_task = asyncio.create_task(self.stats_report())

    async def stats_report(self):
        while self.running:
            await asyncio.sleep(60)
            cpu_percent = psutil.cpu_percent()
            memory_percent = psutil.virtual_memory().percent
            nr_threads = psutil.Process().num_threads()
            nr_tasks = len(asyncio.all_tasks())
            stats = self.lp_cache.stats() | {
                "CPU": cpu_percent,
                "Tasks": nr_tasks,
                "Threads": nr_threads,
                "Memory": memory_percent
            }
            logger.info(", ".join([f"{k}: {v}" for k, v in stats.items()]))

    async def shutdown(self):
        self.running = False
        if hasattr(self, 'block_stream'):
            self.block_stream.shutdown()
        if hasattr(self, 'lp_cache'):
            self.lp_cache.shutdown()
        if hasattr(self, 'aiohttp_session'):
            await self.aiohttp_session.close()
        if hasattr(self, 'token_db'):
            await self.token_db.async_del()
        logger.info("Exited.")

    # If wait=true and block_number is > self.last_block.number, then wait for it
    async def get_lps_trading_tokens(self, token_ids: set, block_number=None, wait=False) -> List[LP]:
        # Might be true when still initializing.
        if self.last_block is None or self.last_block.number is None:
            return []

        if block_number is None or block_number <= self.last_block.number or not wait:
            return self.lp_cache.get_lps_trading_tokens(token_ids, block_number)

        await self.wait_for_block(block_number)
        
        # Should not be necessary to wait a bit since the subscriptions are executed in FIFO order.
        return self.lp_cache.get_lps_trading_tokens(token_ids, block_number)

    def get_order_lps(self, block_number=None) -> List[LP]:
        return self.lp_cache.get_order_lps(block_number)

    # If wait=true and block_number is > self.last_block.number, then wait for it
    async def get_all_lps(self, block_number=None, wait=False) -> List[LP]:
        # Might be true when still initializing.
        if self.last_block is None or self.last_block.number is None:
            return []

        if block_number is None or block_number <= self.last_block.number or not wait:
            return self.lp_cache.get_all_lps(block_number)

        await self.wait_for_block(block_number)
        
        # Should not be necessary to wait a bit since the subscriptions are executed in FIFO order.
        return self.lp_cache.get_all_lps(block_number)

    def update_token_ids(self, token_ids: Set[str]):
        self.lp_cache.update_token_ids(token_ids)

    async def wait_for_block(self, block_number: Optional[int] = None) -> BlockId:
        event = asyncio.Event() 
        async def waiter(block: BlockId):
            if block_number is None:
                event.set()
            elif block.number >= block_number:
                event.set()
        self.block_stream.subscribe(waiter)
        await event.wait()
        self.block_stream.unsubscribe(waiter)
        if block_number is not None and self.last_block.number != block_number:
            raise RuntimeError("Waited for a block that never happened, or was lost. Aborting ...")
        return self.last_block
        
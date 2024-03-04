import asyncio
import logging
import os
import sys
import traceback
from typing import Any, List

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
from lpbook.LPCache import LPCache
from lpbook.LPHistoric import LPHistoric
from lpbook.execution.LPExecution import LPExecution
from lpbook.lps.curve import CurveDriver
from lpbook.lps.uniswap_v3 import UniV3Driver
from lpbook.lps.uniswap_v2 import SushiDriver, UniV2Driver
from lpbook.lps.maker_psm import MakerPSMDriver
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import ServerFilteredEventStream
from pydantic_settings import BaseSettings
from web3 import Web3
from contextlib import asynccontextmanager
import argparse
from .ProcessServer import ProcessServer
from lpbook.util.rpc import create_in_another_process
from lpbook import execution
import lpbook.util.prometheus
import prometheus_async.aio
from aiodebug import log_slow_callbacks
from prometheus_client import start_http_server

logger = logging.getLogger(__name__)

process_servers = None
lp_blacklister = None

# ++++ Interface definition ++++


# Server settings: Can be overriden by passing them as env vars or in a .env file.
# Example: PORT=8001 python -m src._server
class ServerSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8000

    class Config:
        env_file = '.env'


server_settings = ServerSettings()

async def monitor_event_loop_lag(loop: asyncio.AbstractEventLoop):
    start = loop.time()
    sleep_interval = 1
    logger.info("Running event loop lag monitor ...")
    while loop.is_running():
        await asyncio.sleep(sleep_interval)
        diff = loop.time() - start
        lag = diff - sleep_interval
        # send lag as a statsd metric
        if lag > 1:
            tasks = asyncio.all_tasks(loop)
            for task in tasks:
              if task._coro.cr_code.co_name != "monitor_event_loop_lag":
                  logger.warn(f"Event loop lag:{lag}, task: {task}")
        start = loop.time()

async def async_wrapper(fn, *args, **kwargs):
    if asyncio.iscoroutinefunction(fn):
        return await fn(*args, **kwargs)
    else:
        return fn(*args, **kwargs)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Prometheus")
    prometheus_server = asyncio.create_task(asyncio.to_thread(start_http_server,9090))
    logger.info("Starting LPBook ...")
    for process_server in process_servers:
        process_server.start()
    
    if lp_blacklister is not None:
        await lp_blacklister.async_init()

    if profiling:
    #    loop = asyncio.get_running_loop()
    #    loop.create_task(monitor_event_loop_lag(loop))
        log_slow_callbacks.enable(1)
        #dumper = hang_inspection.start('/app/profile')
        #asyncio.ensure_future(hang_inspection.stop_wait(dumper)) 
    
    try:
        yield
    except:
        pass

    await async_wrapper(process_server.shutdown)
    if lp_blacklister is not None:
        await lp_blacklister.async_del()
    logger.info("Exiting LPBook ...")

app = FastAPI(
    title="LPBook service",
    lifespan=lifespan
)


@app.get("/health", status_code=200)
def health():
    """Convenience endpoint to check if server is alive."""
    return True


@app.post("/lps_trading_tokens")
@prometheus_async.aio.time(lpbook.util.prometheus.lps_trading_tokens_time)
async def lps_trading_tokens(token_ids: List[str]) -> dict:
    """Return LPs that trade at least two tokens in the given token list."""
    if len(process_servers) == 0:
        return {}
    try:
        lps = []
        last_block = process_servers[0].last_block
        for process_server in process_servers:
            for lp in await async_wrapper(process_server.get_lps_trading_tokens, {
                token_id.lower()
                for token_id in token_ids
            }):
                lps.append(lp.marshall())
        return {
            "lps": lps,
            "prev_block_number": last_block.number,
            "prev_block_hash": last_block.hash,
        } 
    except Exception as e:
        logger.error(
            f"Unhandled exception: {str(e)}. Traceback:\n{traceback.format_exc()}\n")
        return {}


@app.post("/inspect_lps")
async def inspect_lps(lp_executions: list[LPExecution]) -> None:
    try:
        await lp_blacklister.inspect_lps(lp_executions)
        return True
    except Exception as e:
        logger.error(
            f"Unhandled exception: {str(e)}. Traceback:\n{traceback.format_exc()}\n")
        return False


# ++++ Server setup: ++++


if __name__ == '__main__':
    # Load local environment variables from .env file.
    load_dotenv()

    logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)

    parser = argparse.ArgumentParser(
        prog='LPBook server',
        description='Serves requests for on/off chain liquidity state information'
    )

    class SplitArgs(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, values.split(','))

    parser.add_argument(
        'protocols', 
        type=str, 
        action=SplitArgs, 
        help="Comma separated list of protocols to serve (univ2, pancakeswapv2, sushi, univ3, pancakeswapv3, curve, markerpsm, native, hashflow, balancerv2)."
    )

    parser.add_argument(
        '--profile', 
        action='store_true',
        default=False, 
        help="Enable profiler."
    )

    args = parser.parse_args()

    protocols = args.protocols
    profiling = args.profile

    p = ProcessServer(args.protocols, args.profile)
    #p = create_in_another_process(ProcessServer, args.protocols, args.profile)
    process_servers = [p]
    
    lp_blacklister = execution.LPBlacklister()

    #start_http_server(port=server_settings.port, addr=server_settings.host)

    uvicorn.run(
        "__main__:app",
        host=server_settings.host,
        port=server_settings.port,
        log_level="warning",
        loop='asyncio'
    )

import asyncio
import logging
from pathlib import Path
from typing import  List, Optional, Set

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from lpbook.execution.LPExecution import LPExecution
from pydantic_settings import BaseSettings
from contextlib import asynccontextmanager
import argparse

from lpbook.server.WebsocketDriver import WebsocketDriver
from lpbook.server.util import create_lps_response, create_order_lps_response
from lpbook.web3 import BlockId
from .ProcessServer import ProcessServer
from lpbook import execution
import lpbook.util.prometheus
import prometheus_async.aio
from aiodebug import log_slow_callbacks
from prometheus_client import start_http_server

logger = logging.getLogger(__name__)

process_server = None
lp_stats = None
websocket_driver = None

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
                  logger.warning(f"Event loop lag:{lag}, task: {task}")
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

    #websocket_driver_task = asyncio.create_task(websocket_driver.run())
    process_server.subscribe_on_sync(websocket_driver.run_once)

    # To be on the safe side, we kick out all websocket connections whenever we need to reset process_server,
    # which should happen only if there an unhandled exception.
    process_server.subscribe_on_reset(websocket_driver.disconnect_all)

    logger.info("Starting LPBook ...")
    process_server.start()
    
    if lp_stats is not None:
        await lp_stats.async_init()

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

    prometheus_server.cancel()
    await async_wrapper(process_server.shutdown)
    if lp_stats is not None:
        await lp_stats.async_del()
    logger.info("Exited LPBook ...")

app = FastAPI(
    title="LPBook service",
    lifespan=lifespan
)


@app.get("/health", status_code=200)
def health():
    """Convenience endpoint to check if server is alive."""
    return True


async def lps_trading_tokens_helper(token_ids: List[str], block_number: Optional[int] = None) -> dict:
    token_ids = {token_id.lower() for token_id in token_ids}
    if block_number is not None and block_number > process_server.last_block.number:
        wait = True
        block_hash = None
        block_timestamp = None
    else:
        wait = False
        block_number = process_server.last_block.number
        block_hash = process_server.last_block.hash
        block_timestamp = process_server.last_block.timestamp

    lps = []
    for lp in await async_wrapper(process_server.get_lps_trading_tokens, token_ids, block_number=block_number, wait=wait):
        if lp_stats.blacklisted(lp.uid):
            continue
        lps.append(lp)

    if wait == True:
        block_hash = process_server.last_block.hash
        block_timestamp = process_server.last_block.timestamp

    return create_lps_response(lps, block_number, block_hash, block_timestamp, lp_stats, process_server.lp_cache)

    
async def lps_trading_tokens(token_ids: List[str], block_number: Optional[int] = None) -> dict:
    """Return LPs that trade at least two tokens in the given token list."""
    if process_server is None:
        return {}
    # This can happen if we are still initializing and didn't yet get any block.
    if block_number is None and process_server.last_block.number is None:
        return {}
    try:
        return await lps_trading_tokens_helper(token_ids=token_ids, block_number=block_number)
    except Exception as e:
        logger.exception(f"Unhandled exception when processing /lps_trading_tokens request.")
        lpbook.util.prometheus.error.labels(error_type=str(e)).inc(1)
        return {}
    
@app.post("/lps_trading_tokens")
@prometheus_async.aio.time(lpbook.util.prometheus.lps_trading_tokens_time)
async def lps_trading_tokens_at_current_block(token_ids: List[str]) -> dict:
    return await lps_trading_tokens(token_ids=token_ids)    

@app.post("/lps_trading_tokens_at_block")
async def lps_trading_tokens_at_block(token_ids: List[str], block_number: int) -> dict:
    return await lps_trading_tokens(token_ids=token_ids, block_number=block_number) 


@app.post("/order_lps")
@prometheus_async.aio.time(lpbook.util.prometheus.order_lps_time)
async def order_lps() -> dict:
    """Return LPs that trade at least two tokens in the given token list."""
    if process_server is None:
        return {}
    # This can happen if we are still initializing and didn't yet get any block.
    if process_server.last_block.number is None:
        return {}
    try:
        last_block = process_server.last_block
        order_lps = [
            lp
            for lp in await async_wrapper(process_server.get_order_lps, block_number=last_block.number)
        ]
        return create_order_lps_response(order_lps, last_block) 
    
    except Exception as e:
        logger.exception("Unhandled exception when processing /order_lps request.")
        lpbook.util.prometheus.prometheus.error.labels(error_type=str(e)).inc(1)
        return {}

background_tasks = set()

@app.post("/on_reverted_solution")
async def on_reverted_solution(lp_executions: list[LPExecution]) -> None:
    async def run_on_background():
        try:
            nr_successes = await lp_stats.update(lp_executions)
            if nr_successes is not None and nr_successes == len(lp_executions):
                logger.warning(f"All executions passed to /on_reverted_solution simulated successfully:\n{lp_executions}")
        except Exception as e:
            logger.exception("Unhandled exception when processing /on_reverted_solution request.")
    task = asyncio.create_task(run_on_background())
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)
    return True

@app.post("/on_submitted_solution")
async def on_submitted_solution(lp_executions: list[LPExecution]) -> None:
    logger.debug(f"Received {len(lp_executions)} LP executions: {lp_executions}")
    async def run_on_background():
        try:
            await lp_stats.update(lp_executions)
        except Exception as e:
            logger.exception("Unhandled exception when processing /on_submitted_solution request.")
    task = asyncio.create_task(run_on_background())
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)
    return True

@app.websocket("/ws_latest")
async def websocket_endpoint(websocket: WebSocket):
    logger.debug(f"New websocket connection.")
    await websocket_driver.connect(websocket)
    try:
        while True:
            token_ids = await websocket.receive_json()
            process_server.update_token_ids(token_ids)
    except WebSocketDisconnect:
        logger.debug(f"Websocket client disconnected. Removing connection.")
        websocket_driver.disconnect(websocket)
        logger.debug(f"Removed connection.")
    except Exception:
        logger.exception(f"Unhandled exception in websocket endpoint. Dropping connection.")
        websocket_driver.disconnect(websocket)

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
        'state_directory',
        type=Path,
        help="Directory to store app state."
    )

    parser.add_argument(
        'protocols', 
        type=str, 
        action=SplitArgs, 
        help="Comma separated list of protocols to serve (univ2, pancakeswapv2, sushi, univ3, "
        "pancakeswapv3, curve, native, hashflow, balancerv2, cowammbalancer, fixedrate, cowammprivate)."
    )

    parser.add_argument(
        '--mandatory_univ3_amms', 
        type=str, 
        action=SplitArgs,
        default=[],
        help="Comma separated list of univ3 amm ids to always include, if they are cached."
    )

    parser.add_argument(
        '--mandatory_univ2_amms', 
        type=str, 
        action=SplitArgs,
        default=[],
        help="Comma separated list of univ2 amm ids to always include, if they are cached."
    )

    parser.add_argument(
        '--profile', 
        action='store_true',
        default=False, 
        help="Enable profiler."
    )

    args = parser.parse_args()

    protocols = args.protocols
    mandatory_amms = {
        "Uniswap_3": set(args.mandatory_univ3_amms),
        "Uniswap_2": set(args.mandatory_univ2_amms)
    }
    profiling = args.profile
    
    lp_stats = execution.LPStats(args.state_directory)

    process_server = ProcessServer(protocols, mandatory_amms, args.state_directory, profiling)
    #p = create_in_another_process(ProcessServer, args.protocols, args.profile)
    
    websocket_driver = WebsocketDriver(lp_stats, process_server)

    uvicorn.run(
        "__main__:app",
        host=server_settings.host,
        port=server_settings.port,
        log_level="warning",
        loop='asyncio'
    )

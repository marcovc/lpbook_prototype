import asyncio
import logging
import os
import sys
import traceback
from typing import List

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
from lpbook.LPCache import LPCache
from lpbook.LPHistoric import LPHistoric
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

logger = logging.getLogger(__name__)

aiohttp_session = None
lp_cache = None
lp_historic = None
protocols = []

# ++++ Interface definition ++++


# Server settings: Can be overriden by passing them as env vars or in a .env file.
# Example: PORT=8001 python -m src._server
class ServerSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8000

    class Config:
        env_file = '.env'


server_settings = ServerSettings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting LPBook ...")
    asyncio.ensure_future(reset_on_error())
    yield
    await aiohttp_session.close()
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
async def lps_trading_tokens(token_ids: List[str]):
    """Return LPs that trade at least two tokens in the given token list."""
    try:
        return [
            lp.marshall()
            for lp in lp_cache.get_lps_trading_tokens({
                token_id.lower()
                for token_id in token_ids
            })
        ]
    except Exception as e:
        logger.error(
            f"Unhandled exception: {str(e)}. Traceback:\n{traceback.format_exc()}\n")
        return []


@app.post("/lps_trading_tokens_historic")
async def lps_trading_tokens_historic(token_ids: List[str], block_number: int):
    """Return LPs that trade at least two tokens in the given token list at given block."""
    try:
        return [
            lp.marshall()
            for lp in await lp_historic.get_lps_trading_tokens(
                {
                    token_id.lower()
                    for token_id in token_ids
                },
                block_number=block_number
            )
        ]
    except Exception as e:
        logger.error(
            f"Unhandled exception: {str(e)}. Traceback:\n{traceback.format_exc()}\n")
        return []


async def reset():
    global aiohttp_session    
    global lp_cache
    global lp_historic
    global protocols

    logger.info("Resetting LPBook ...")

    HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
    WS_WEB3_URL = os.getenv('WS_WEB3_URL')

    import requests
    requests_adapter = requests.adapters.HTTPAdapter(pool_connections=20, pool_maxsize=20)
    requests_session = requests.Session()
    requests_session.mount('http://', requests_adapter)
    requests_session.mount('https://', requests_adapter)
    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL, session=requests_session))

    block_stream = BlockStream(WS_WEB3_URL)
    event_stream = ServerFilteredEventStream(block_stream, w3)
    aiohttp_session = aiohttp.ClientSession()

    drivers = []

    # LP drivers
    if "univ3" in protocols:
        drivers.append(UniV3Driver(event_stream, block_stream, aiohttp_session, w3))
    if "curve" in protocols:
        drivers.append(CurveDriver(block_stream, aiohttp_session, w3))
    if "univ2" in protocols:
        drivers.append(UniV2Driver(event_stream, block_stream, aiohttp_session, w3))
    if "sushi" in protocols:
        drivers.append(SushiDriver(event_stream, block_stream, aiohttp_session, w3))
    if "makerpsm" in protocols:
        drivers.append(MakerPSMDriver())

    for driver in drivers:
        logger.info(f"Enabled driver {driver.__class__.__name__}.")

    # Create LP Cache (main service)
    # Returns current state (fast).
    
    lp_cache = LPCache(drivers)

    # Create LP Historic (main service)
    # Returns past state (slow).
    # lp_historic = LPHistoric([univ3_driver, sushi_driver, curve_driver])

    await asyncio.gather(
        block_stream.run(),
        lp_cache.run()
    )


async def reset_on_error():
    while True:
        try:
            await reset()
        except Exception as e:
            logger.error(
                f"Received unhandled exception: {str(e)}. Resetting."
                f"Traceback:\n{traceback.format_exc()}\n"
            )
    

# ++++ Server setup: ++++


if __name__ == '__main__':
    # Load local environment variables from .env file.
    load_dotenv()

    logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)

    load_dotenv()

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
        help="Comma separated list of protocols to serve (univ2, sushi, univ3, curve, markerpsm)."
    )

    args = parser.parse_args()

    protocols = args.protocols

    uvicorn.run(
        "__main__:app",
        host=server_settings.host,
        port=server_settings.port,
        log_level="warning",
        loop='asyncio'
    )

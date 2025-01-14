
import asyncio
import logging.config
import os

import aiohttp
from dotenv import load_dotenv
from lpbook import LPDriver
from lpbook.lps.curve_old import CurveDriver
from lpbook.lps.uniswap_v3 import UniV3Driver
from lpbook.lps.uniswap_v2 import UniV2Driver
from lpbook.util import traced_context
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream
from lpbook.web3.event_stream import ServerFilteredEventStream
from web3 import Web3

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)

logger = logging.getLogger(__name__)

load_dotenv()

HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
WS_WEB3_URL = os.getenv('WS_WEB3_URL')


async def assert_equivalent_proxies(
    web3_client,
    oracle_proxy,
    testing_proxy,
    block_stream,
    block_lag=0
):
    """Tests if two different proxies yield exactly the same results.

    The oracle_proxy is allowed to raise an exception, but must yield correct results
    when it does not (typically it is an async proxy).

    The testing_proxy is not allowed to raise exceptions.
    """

    async def check_at_block(block: BlockId):
        assert block.number is not None
        logger.debug(
            f'Asserting equivalent state at block {block} ...'
        )
        try:
            lps1 = oracle_proxy(block)
        except RuntimeError as err:
            logger.warning(
                f'Could not query oracle proxy at {cur_block_number}: {err}. '
                'Possibly skipping block ...'
            )
            return
        lps2 = testing_proxy(block)
        lps1 = {lp_id: lps1[lp_id] for lp_id in sorted(lps1.keys())}
        lps2 = {lp_id: lps2[lp_id] for lp_id in sorted(lps2.keys())}
        if lps1 != lps2:
            for lp1, lp2 in zip(lps1.values(), lps2.values()):
                if lp1 != lp2:
                    print('different elements:')
                    print('oracle:', lp1)
                    print('testing:', lp2)
            if len(lps1) != len(lps2):
                print('only 1:', set(lps1)-set(lps2))
                print('only 2:', set(lps2)-set(lps1))
            assert(False)

    cur_block = web3_client.eth.get_block('latest')
    logger.debug(f'Latest block is {cur_block.number}')

    with traced_context(logger, 'Starting proxies'):
        await oracle_proxy.start()
        await testing_proxy.start()

    with traced_context(
        logger,
        f'Starting block index at block {cur_block.number - block_lag}'
    ):
        asyncio.ensure_future(block_stream.run(cur_block.number - block_lag))

    # wait until all caches are filled
    with traced_context(logger, 'Cache warm up'):
        while block_stream.last_block is None or block_stream.last_block.number is None  or \
                block_stream.last_block.number < cur_block.number:
            await asyncio.sleep(5)

    with traced_context(logger, 'Main run loop'):
        while True:
            cur_block_number = block_stream.last_block.number - block_lag
            if block_lag == 0:
                cur_block_hash = block_stream.last_block.hash
            else:
                cur_block = web3_client.eth.get_block(cur_block_number)
                cur_block_hash = cur_block.hash.hex()
            await check_at_block(BlockId(number=cur_block_number, hash=cur_block_hash))
            await asyncio.sleep(10)


async def test_uniswap_v3():

    token_ids = {
        '0x6b175474e89094c44da98b954eedeac495271d0f',
        '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
    }

    # w3 = Web3(Web3.WebsocketProvider(WS_WEB3_URL))
    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))

    block_stream = BlockStream(WS_WEB3_URL)
    event_stream = ServerFilteredEventStream(block_stream, w3)
    async with aiohttp.ClientSession() as session:
        driver = UniV3Driver(event_stream, block_stream, session, w3)

        lp_ids = await driver.get_lp_ids(token_ids)
        proxy_thegraph = driver.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.TheGraph
        )
        proxy_web3 = driver.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        )

        await assert_equivalent_proxies(w3, proxy_thegraph, proxy_web3, block_stream, 10)


# This is currently not working, since the curve subgraph apparently is not handling
# the ramp of the amplification coefficient correctly. So if this change is currently in
# progress for some AMM, then the tests will give false failures.
# (here we're using TheGraph as the oracle)
# https://github.com/curvefi/curve-subgraph/issues/11.
async def test_curve():
    token_ids = {
        '0x6b175474e89094c44da98b954eedeac495271d0f',
        '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'.lower()
    }

    # w3 = Web3(Web3.WebsocketProvider(WS_WEB3_URL))
    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))

    block_stream = BlockStream(WS_WEB3_URL)
    async with aiohttp.ClientSession() as session:
        driver = CurveDriver(block_stream, session, w3)

        lp_ids = await driver.get_lp_ids(token_ids)
        proxy_thegraph = driver.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.TheGraph
        )
        proxy_web3 = driver.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.Web3
        )

        await assert_equivalent_proxies(w3, proxy_thegraph, proxy_web3, block_stream, 10)


async def test_uniswap_v2():
    token_ids = {
        '0x6982508145454ce325ddbe47a25d4ec3d2311933',
        '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'.lower()
    }

    # w3 = Web3(Web3.WebsocketProvider(WS_WEB3_URL))
    w3 = Web3(Web3.HTTPProvider(HTTP_WEB3_URL))

    block_stream = BlockStream(WS_WEB3_URL)
    event_stream = ServerFilteredEventStream(block_stream, w3)
    async with aiohttp.ClientSession() as session:
        driver = UniV2Driver(event_stream, block_stream, session, w3)

        lp_ids = await driver.get_lp_ids(token_ids)
        proxy_thegraph = driver.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.TheGraph
        )
        proxy_web3 = driver.create_lp_sync_proxy(
            lp_ids,
            LPDriver.LPSyncProxyDataSource.TheGraphAndWeb3
        )

        await assert_equivalent_proxies(w3, proxy_thegraph, proxy_web3, block_stream, 10)

#asyncio.run(test_uniswap_v3())
# asyncio.run(test_curve())
asyncio.run(test_uniswap_v2())

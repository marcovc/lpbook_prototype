
import asyncio
from typing import List
import aiohttp

from web3 import AsyncWeb3
from web3.exceptions import BlockNotFound

from lpbook.execution.LPExecution import LPExecution
import os
import logging
from .simulation import Simulator, NoConnectionException, FailedBuyTransactionException, NoStateDiffException
from dotenv import load_dotenv

from lpbook.web3 import BlockId

load_dotenv()

logger = logging.getLogger(__name__)

HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
WS_WEB3_URL = os.getenv('WS_WEB3_URL')

SETTLEMENT_ADDRESS = "0x9008d19f58aabd9ed0d60971565aa8510560ab41"

class LPBlacklister:
    def __init__(self):
        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(HTTP_WEB3_URL))
        #w3 = AsyncWeb3(AsyncWeb3.AsyncWebsocketProvider(WS_WEB3_URL))

    # aiohttp.ClientSession needs to be created from within a coroutine.
    async def async_init(self):
        self.aiohttp_session = aiohttp.ClientSession()
        self.simulator = Simulator(self.w3, self.aiohttp_session, SETTLEMENT_ADDRESS)

    async def async_del(self):
        await self.aiohttp_session.close()

    async def get_succ_block(self, prev_block_hash: str) -> BlockId:
        prev_block = await self.w3.eth.get_block(block_identifier=prev_block_hash)
        succ_block = await self.w3.eth.get_block(block_identifier=prev_block.number + 1)
        return BlockId(number=succ_block.number, hash=succ_block.hash)

    async def inspect_lps(self, lp_executions: List[LPExecution]):
        assert len(lp_executions) > 0
        prev_block_hash = lp_executions[0].prev_block_hash
        try:
            succ_block = await self.get_succ_block(prev_block_hash)
        except BlockNotFound:
            return
        to_blacklist = []
        some_simulation_failed = False
        for lp_execution in lp_executions:
            try:
                simulation = await self.simulator.simulate_execution(lp_execution=lp_execution, block_number=succ_block.number)
                if not simulation.success:
                    print("would blacklist:",lp_execution.lp_id,simulation.tenderly_url)
                    to_blacklist.append(lp_execution.lp_id)
            except NoConnectionException as e:
                logger.warning(f"Error simulating execution (no connection) {lp_execution}: {str(e)}")
                some_simulation_failed = True
            except FailedBuyTransactionException as e:        
                logger.error(f"Error simulating execution (failed buy transaction) {lp_execution}: {str(e)}")        
                some_simulation_failed = True
            except NoStateDiffException as e:
                logger.error(f"Error simulating execution (no state diff) {lp_execution}: {str(e)}")        
                some_simulation_failed = True
            except Exception as e:
                logger.error(f"Error simulating execution {lp_execution}: {str(e)}")        
                some_simulation_failed = True
        if len(to_blacklist)==0 and not some_simulation_failed:
            logger.warn("All executions simulated successfully: {lp_executions}")
        return to_blacklist
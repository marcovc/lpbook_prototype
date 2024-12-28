
import asyncio
from dataclasses import dataclass
import json
from pathlib import Path
import pickle
from typing import List, Optional, Tuple
import aiohttp

from web3 import AsyncWeb3
from web3.exceptions import BlockNotFound

from lpbook.execution.LPExecution import LPExecution
import os
import logging

from lpbook.util import traced
from .simulation import Simulation, Simulator, NoConnectionException, FailedBuyTransactionException, NoStateDiffException, NoAllowanceKeyException, NoBalanceKeyException
from dotenv import load_dotenv

from lpbook.web3 import BlockId
from math import sqrt
from lpbook.util.prometheus import blacklisted_lps, error
from datetime import datetime, timedelta
import jsonpickle
from .trusted_tokens import trusted_tokens

load_dotenv()

logger = logging.getLogger(__name__)

HTTP_WEB3_URL = os.getenv('HTTP_WEB3_URL')
WS_WEB3_URL = os.getenv('WS_WEB3_URL')

SETTLEMENT_ADDRESS = "0x9008d19f58aabd9ed0d60971565aa8510560ab41"


# Welford's method
class RunningMeanStddev:
    def __init__(self):
        self.n = 0
        self.mean = 0
        self.m2 = 0
    def update(self, value):
        self.n += 1
        delta = value - self.mean
        self.mean += delta / self.n
        self.m2 += delta * (value - self.mean)
    @property
    def stddev(self):
        assert self.n >= 2, "At least two observations are required for computing a stddev."
        return sqrt(self.m2 / (self.n - 1))
          
# Censoring works as follows:
# If an lp fails simulation on original block, it is blacklisted during blacklist_time = BLACKLIST_INIT_DURATION. After that, if it happens
# that it is used again and reverts again, then it is blacklisted again during blacklist_time *= BLACKLIST_BACKOFF_FACTOR.
# Whenever it succeeds, then blacklist_time is reset to 0.
    
class CensoredLPInfo:
    BLACKLIST_INIT_DURATION = timedelta(minutes=10)     # how long to blacklist an lp the first time it reverts
    BLACKLIST_BACKOFF_FACTOR = 10   # multiply time in tabu list by this number each time it reverts

    def __init__(self, lp_execution, failed_tenderly_url):
        self.lp_id = lp_execution.lp_id
        self.protocol = lp_execution.protocol
        self.start = datetime.now()
        self.end = self.start + self.BLACKLIST_INIT_DURATION
        self.auction_id = lp_execution.auction_id
        self.failed_tenderly_url = failed_tenderly_url

    def update(self, auction_id, failed_tenderly_url):
        new_start = datetime.now()
        new_end = new_start + (self.end - self.start) * self.BLACKLIST_BACKOFF_FACTOR
        self.start, self.end = new_start, new_end
        self.auction_id = auction_id
        self.failed_tenderly_url = failed_tenderly_url

    def is_censored(self):
        return datetime.now() <= self.end

    def __getstate__(self):
        d = {**self.__dict__}
        d["start"] = self.start.strftime("%Y-%m-%d %H:%M:%S")
        d["end"] = self.end.strftime("%Y-%m-%d %H:%M:%S")
        return d    

    def __setstate__(self, s):
        self.__dict__ = s
        self.start = datetime.strptime(s["start"], "%Y-%m-%d %H:%M:%S")
        self.end = datetime.strptime(s["end"], "%Y-%m-%d %H:%M:%S")
 
 # Sometimes we can't even simulate a transaction, because we can't get balance keys or something. This is already
 # a warning sign, but some of the pools are legit. In any case, if we see the same lp being sent for inspection
 # more than N times in the last M minutes, we also censor it to avoid getting stuck.
class HitCounter:
    N = 5
    M = 5
    def __init__(self):
        self.hits = []
    def hit(self):
        now = datetime.now()
        self.hits.append(now)
        self.hits = [dt for dt in self.hits if dt >= now - timedelta(minutes=HitCounter.M)]
        return len(self.hits) > HitCounter.N

@dataclass
class GasStatsInfo:
    lp_id: str
    protocol: str
    stats: RunningMeanStddev

class LPStats:
    BLACKLIST_INIT_DURATION = timedelta(minutes=10)     # how long to blacklist an lp the first time it reverts
    BLACKLIST_BACKOFF_FACTOR = 10   # multiply time in tabu list by this number each time it reverts

    def __init__(self, state_directory: Path):
        self.state_directory = state_directory
        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(HTTP_WEB3_URL))
        #w3 = AsyncWeb3(AsyncWeb3.AsyncWebsocketProvider(WS_WEB3_URL))
        self.tabu_list: dict[str, CensoredLPInfo] = {}  
        self.gas_stats: dict[str, GasStatsInfo] = {} 
        self.load_state()
        self.last_block_hash: dict[str, str] = {}
        self.hit_counter: dict[str, HitCounter] = {}

    # aiohttp.ClientSession needs to be created from within a coroutine.
    async def async_init(self):
        self.aiohttp_session = aiohttp.ClientSession()
        self.simulator = Simulator(self.w3, self.aiohttp_session, SETTLEMENT_ADDRESS, self.state_directory, discount_intrinsic_gas=True)
        self.keep_prometheus_up_to_date_task = asyncio.create_task(self.keep_prometheus_up_to_date())

    async def async_del(self):
        await self.aiohttp_session.close()
        self.dump_state()
    
    async def keep_prometheus_up_to_date(self):
        while True:
            for lp_id, censored_info in self.tabu_list.items():
                blacklisted_lps.labels(lp_id=lp_id).set(censored_info.is_censored())
            await asyncio.sleep(120)

    def load_state(self):
        try:
            with open(self.state_directory / "lp_stats_tabu_list.json", "r") as f:
                self.tabu_list = jsonpickle.decode(f.read())
        except FileNotFoundError:
            pass
        try:
            with open(self.state_directory / "lp_stats_gas_stats.json", "r") as f:
                self.gas_stats = jsonpickle.decode(f.read())
        except FileNotFoundError:
            pass
                
    def dump_state(self):
        with open(self.state_directory / "lp_stats_tabu_list.json", "w+") as f:
            f.write(jsonpickle.encode(self.tabu_list))
        with open(self.state_directory / "lp_stats_gas_stats.json", "w+") as f:
            f.write(jsonpickle.encode(self.gas_stats))

    async def get_succ_block(self, prev_block_hash: str) -> BlockId:
        prev_block = await self.w3.eth.get_block(block_identifier=prev_block_hash)
        succ_block = await self.w3.eth.get_block(block_identifier=prev_block.number + 1)
        return BlockId(number=succ_block.number, hash=succ_block.hash, timestamp=succ_block.timestamp)

    def record_simulation(self, lp_execution: LPExecution, simulation: Simulation, block: BlockId):
        lp_id, auction_id = lp_execution.lp_id, lp_execution.auction_id 
        if simulation.success:
            if lp_id in self.tabu_list:
                logger.debug(f"Previously censored LP {lp_id} succeeded simulation on original block. Uncensoring....")
                blacklisted_lps.labels(lp_id=lp_id).set(0)
                self.uncensor(lp_id)
            if lp_id not in self.gas_stats:
                self.gas_stats[lp_id] = GasStatsInfo(lp_id, lp_execution.protocol, RunningMeanStddev())
            if lp_execution.simulated_gas is not None:
                self.gas_stats[lp_id].stats.update(lp_execution.simulated_gas)
            else:
                self.gas_stats[lp_id].stats.update(simulation.gas_used)
        else:
            logger.debug(f"LP {lp_id} failed simulation on original block: {simulation.tenderly_url} . Censoring....")
            blacklisted_lps.labels(lp_id=lp_id).set(1)
            self.censor(lp_execution, simulation.tenderly_url)
    
    # Returns number of successes, unless there was some error with a simulation.
    @traced(logger, "Updating LPStats with new list of lp executions")
    async def update(self, lp_executions: List[LPExecution]) -> Optional[int]:
        assert len(lp_executions) > 0
        prev_block_hash = lp_executions[0].prev_block_hash
        try:
            succ_block = await self.get_succ_block(prev_block_hash)
        except BlockNotFound:
            logger.warning(f"Could not get successor block of block {prev_block_hash}. Either it is too new, or a reorg happened?")
            return None
        some_simulation_failed = False
        nr_successes = 0
        for lp_execution in lp_executions:
            # Do not perform multiple simulations of the same lp in the same block to save tenderly quota and also avoid skewing stats.
            # That is, we assume that if an execution of some lp in some solution passes (resp. reverts) in block B, then another
            # execution of the same lp in some other solution would pass (resp. revert) in block B with same gas. 
            # It is an approximation, but should almost always be the case.
            if lp_execution.lp_id in self.last_block_hash and self.last_block_hash[lp_execution.lp_id] == succ_block.hash:
                continue
            self.last_block_hash[lp_execution.lp_id] = succ_block.hash
            try:
                simulation = await self.simulator.simulate_execution(lp_execution=lp_execution, block_number=succ_block.number)
                self.record_simulation(lp_execution, simulation, succ_block)
                nr_successes += simulation.success
            except NoConnectionException as e:
                logger.warning(f"Error simulating execution (no connection) {lp_execution}: {str(e)}")
                some_simulation_failed = True
            except FailedBuyTransactionException as e:        
                logger.error(f"Error simulating execution (failed buy transaction) {lp_execution}: {str(e)}")        
                some_simulation_failed = True
            except NoStateDiffException as e:
                logger.error(f"Error simulating execution (no state diff) {lp_execution}: {str(e)}")        
                some_simulation_failed = True
            except NoAllowanceKeyException as e:                
                logger.error(f"Error simulating execution (could not compute allowance key) {lp_execution}: {str(e)}")
                if not some_simulation_failed:
                    self.handle_simulation_error(lp_execution)        
                some_simulation_failed = True
            except NoBalanceKeyException as e:
                logger.warn(f"Error simulating execution (could not compute balance key) {lp_execution}: {str(e)}")        
                if not some_simulation_failed:
                    self.handle_simulation_error(lp_execution)        
                some_simulation_failed = True
            except Exception as e:
                logger.exception(f"Error simulating execution {lp_execution}")        
                some_simulation_failed = True

        if not some_simulation_failed:
            return nr_successes
        return None

    def censor(self, lp_execution, tenderly_url):
        if self.censoring_trusted_token(lp_execution, tenderly_url):
            logger.warning(f"LP '{lp_execution.lp_id}' that would be censored trades only trusted tokens. This is probably a false positive. Simulation: {tenderly_url}")
            error.labels(error_type="censoring_trusted_tokens").inc(1)
            return
        if lp_execution.lp_id not in self.tabu_list:
            self.tabu_list[lp_execution.lp_id] = CensoredLPInfo(lp_execution, tenderly_url)
        else:
            self.tabu_list[lp_execution.lp_id].update(lp_execution.auction_id, tenderly_url)

    def uncensor(self, lp_id):
        self.tabu_list.pop(lp_id, None)

    def censoring_trusted_token(self, lp_execution, tenderly_url):
        return len({lp_execution.buy_token_address, lp_execution.sell_token_address} & trusted_tokens) == 2

    def blacklisted(self, lp_id):
        if lp_id not in self.tabu_list:
            return False
        return self.tabu_list[lp_id].is_censored()
    
    def gas_mean_and_stddev(self, lp_id) -> Optional[Tuple[float, float]]:
        if lp_id not in self.gas_stats or self.gas_stats[lp_id].stats.n <= 2:
            return None
        return self.gas_stats[lp_id].stats.mean, self.gas_stats[lp_id].stats.stddev

    def handle_simulation_error(self, lp_execution):
        if not self.hit_counter.setdefault(lp_execution.lp_id, HitCounter()).hit():
            return
        logger.warning(f"Lp {lp_execution.lp_id} has been hitting the simulator repeatedly. Censoring it even if it can't be simulated on the original block.")
        self.censor(lp_execution, None)
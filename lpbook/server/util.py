
import datetime
from typing import Any, List

from lpbook.execution import LPStats
from lpbook.server.ProcessServer import ProcessServer
from lpbook.web3 import BlockId


def marshal_lp(lp: Any, lp_stats: LPStats) -> dict:
    marshalled = lp.marshall()
    gas_mean_and_stddev = lp_stats.gas_mean_and_stddev(lp.uid)
    if gas_mean_and_stddev is not None:
        marshalled["gas_stats"]["mean"], marshalled["gas_stats"]["stddev"] = gas_mean_and_stddev
    return marshalled

def create_lps_response(lps: List[Any], block_number: int, block_hash: str, block_timestamp: int, wait: bool, lp_stats: LPStats, process_server: ProcessServer) -> List[dict]:
    marshalled_lps = [marshal_lp(lp, lp_stats) for lp in lps]
    if process_server.last_block is not None:
        block_time = process_server.last_block.datetime() if wait else datetime.datetime.fromtimestamp(block_timestamp)
        expected_average_xrates_in_running_hour = process_server.estimate_average_xrate_in_running_hour_for_all_token_pairs(
            lps, block_number=block_number, block_time=block_time
        )
    else:
        expected_average_xrates_in_running_hour = {}

    return {
        "lps": marshalled_lps,
        "prev_block_number": block_number,
        "prev_block_hash": process_server.last_block.hash.to_0x_hex() if wait else block_hash.to_0x_hex(),
        "prev_block_timestamp": process_server.last_block.timestamp if wait else block_timestamp,
        "expected_average_xrates_in_running_hour": expected_average_xrates_in_running_hour
    } 


def create_order_lps_response(order_lps: List[Any], block: BlockId) -> dict:
    marshalled_order_lps = [lp.marshall() for lp in order_lps]
    return {
        "order_lps": marshalled_order_lps,
        "prev_block_number": block.number,
        "prev_block_hash": block.hash.to_0x_hex(),
        "prev_block_timestamp": block.timestamp
    }


import datetime
from typing import Any, List, Optional, Tuple

from hexbytes import HexBytes

from lpbook import LPCache
from lpbook.execution import LPStats
from lpbook.server.ProcessServer import ProcessServer
from lpbook.util import LP
from lpbook.web3 import BlockId


def marshal_lp(lp: LP, lp_stats: LPStats) -> dict:
    marshalled = lp.marshall()
    gas_mean_and_stddev = lp_stats.gas_mean_and_stddev(lp.uid)
    if gas_mean_and_stddev is not None:
        marshalled["gas_stats"]["mean"], marshalled["gas_stats"]["stddev"] = gas_mean_and_stddev
    return marshalled

def create_lps_response(
        lps: List[LP], 
        block_number: int, 
        block_hash: HexBytes, 
        block_timestamp: int, 
        lp_stats: LPStats, 
        lp_cache: LPCache
) -> List[dict]:
    marshalled_lps = [marshal_lp(lp, lp_stats) for lp in lps]
    expected_average_xrates_in_running_hour = create_estimate_average_xrate_in_running_hour_for_all_token_pairs_response(
        lp_cache, lps, block_number=block_number, block_time=datetime.datetime.fromtimestamp(block_timestamp)
    )

    return {
        "lps": marshalled_lps,
        "prev_block_number": block_number,
        "prev_block_hash": block_hash.to_0x_hex(),
        "prev_block_timestamp": block_timestamp,
        "expected_average_xrates_in_running_hour": expected_average_xrates_in_running_hour
    } 


def create_order_lps_response(order_lps: List[LP], block: BlockId) -> dict:
    marshalled_order_lps = [lp.marshall() for lp in order_lps]
    return {
        "order_lps": marshalled_order_lps,
        "prev_block_number": block.number,
        "prev_block_hash": block.hash.to_0x_hex(),
        "prev_block_timestamp": block.timestamp
    }


def create_estimate_average_xrate_in_running_hour_for_all_token_pairs_response(
    lp_cache, 
    lps: List[LP], 
    block_number: int, 
    block_time: datetime.datetime
) -> list[Tuple[str, str, float, Optional[float]]]:
    r = lp_cache.estimate_average_xrate_in_running_hour_for_all_token_pairs(lps, block_number=block_number, block_time=block_time)
    return [
        (t1t2[0].address, t1t2[1].address, *v) for (t1t2, v) in r.items()
    ]
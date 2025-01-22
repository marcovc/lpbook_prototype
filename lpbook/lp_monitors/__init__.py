from itertools import permutations
import logging

from lpbook.util import LP, Token, Trade

from dotenv import load_dotenv  

from .amounts import TradedAmountsCollectors
from .slippage import SlippageEstimators

import os

load_dotenv()

USE_LP_MONITORS = os.getenv('USE_LP_MONITORS', 'true').lower() == 'true'
LP_MONITOR_WINDOW_SIZE = int(os.getenv('LP_MONITOR_WINDOW_SIZE', 300))
SLIPPAGE_QUANTIZATION = int(os.getenv('SLIPPAGE_QUANTIZATION', 4))

logger = logging.getLogger(__name__)


class LPMonitors:
    def __init__(self):
        #self.slippage_estimators = SlippageEstimators(LP_MONITOR_WINDOW_SIZE, SLIPPAGE_QUANTIZATION)
        self.traded_amount_collectors = TradedAmountsCollectors(LP_MONITOR_WINDOW_SIZE)

    def record_trade(self, trade: Trade):
        #self.slippage_estimators.record_buy_amounts(lp_uid=lp_uid, block=block, tokens=[token1, token2], buy_amounts=[buy_amount1, buy_amount2])
        self.traded_amount_collectors.record_trade(trade)
        
    def initialize(self, lp: LP, block: int):
        #self.slippage_estimators.initialize(lp_uid=lpuid, block=block, tokens=tokens)
        self.traded_amount_collectors.initialize(lp, block)


# TODO: load/save state
lp_monitors = LPMonitors() if USE_LP_MONITORS else None


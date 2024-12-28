from math import ceil
from typing import Optional
import logging

from lpbook.util import Token

from dotenv import load_dotenv  
import os

load_dotenv()


logger = logging.getLogger(__name__)

class SlippageEstimator:
    def __init__(self, window_size: int, quantization: int, block: int):
        self.window_size= window_size
        self.quantization = quantization
        self.last_block = block
        self.observations = [0]

    def record_buy_amount(self, block: int, buy_amount: int):
        if self.last_block is not None and block < self.last_block:
            return # For slippage estimation purposes, we don't care about reorgs
        if self.last_block is None:
            self.observations = [0]
        else:
            # this appends nothing if block <= self.last_block
            self.observations += [0] * (block - self.last_block)
        self.observations[-1] += buy_amount
        self.observations = self.observations[-2*self.window_size:] # keep twice the requested window size to allow for reorgs
        self.last_block = block

    def quantized(self, data):
        r = sum(data[:self.quantization])
        if len(data) >= self.quantization:
            yield r
        for i in range(self.quantization, len(data)):
            r -= data[i - self.quantization]
            r += data[i]
            yield r

    def estimate_quantile_empirical(self, data, q) -> Optional[int]:
        data = list(data)
        if len(data) == 0:
            return None
        return sorted(data)[min(ceil(len(data) * q), len(data) - 1)]

    def estimate(self, block: int, risk: float) -> Optional[float]:
        # Since we update observations lazily, we also need to update it here
        self.record_buy_amount(block, 0)
        if len(self.observations) < self.window_size:
            return None # Only provide an estimate when there is enough confidence
        quantized = self.quantized(self.observations[-self.window_size:])
        quantile = 1 - risk
        return self.estimate_quantile_empirical(quantized, quantile)

    def estimate_signal(self, block: int, nr_observations: Optional[int] = None) -> Optional[float]:
        # Since we update observations lazily, we also need to update it here
        self.record_buy_amount(block, 0)
        if nr_observations == None:
            nr_observations = self.window_size
        if len(self.observations) < self.window_size:
            return None # Only provide an estimate when there is enough confidence
        total_bought = sum(obs for obs in self.observations[-nr_observations:] if obs > 0)
        total_sold = sum(-obs for obs in self.observations[-nr_observations:] if obs < 0)
        if total_bought == 0 and total_sold == 0:
            return 1
        if total_bought == 0:
            return 10000 # just a very large number to stand for +oo
        return total_sold / total_bought


class SlippageEstimators:
    def __init__(self, window_size: int, quantization: int):
        self.window_size = window_size
        self.quantization = quantization
        self.estimators = {}

    def record_buy_amount(self, lp_uid: str, block: int, token: Token, buy_amount: int):
        if (lp_uid, token) not in self.estimators:
            self.estimators[lp_uid, token] = SlippageEstimator(self.window_size, self.quantization)
        self.estimators[lp_uid, token].record_buy_amount(block, buy_amount)

    def record_buy_amounts(self, lp_uid: str, block: int, tokens: list[Token], buy_amounts: list[int]):
        assert len(tokens) == len(buy_amounts)
        for token, buy_amount in zip(tokens, buy_amounts):
            self.record_buy_amount(lp_uid=lp_uid, block=block, token=token, buy_amount=buy_amount)

    def estimate(self, lp_uid: str, token: Token, block: int, risk: float) -> Optional[float]:
        if (lp_uid, token) not in self.estimators:
            self.estimators[lp_uid, token] = SlippageEstimator(self.window_size, self.quantization, block)
        estimator = self.estimators[lp_uid, token]
        r = estimator.estimate(block, risk)
        if r is None:
            logger.debug(f"LP {lp_uid} has no slippage information yet, since only {len(estimator.observations)}/{estimator.window_size} observations were collected.")
        return r

    def estimates(self, lp_uid: str, block: int, tokens: list[Token], risk: float) -> Optional[float]:
        r = {token: self.estimate(lp_uid=lp_uid, token=token, block=block, risk=risk) for token in tokens}
        r = {k: v for k, v in r.items() if v is not None}
        if len(r) == 0:
            return None
        return r

    def estimate_signal(self, lp_uid: str, token: Token, block: int) -> Optional[float]:
        if (lp_uid, token) not in self.estimators:
            self.estimators[lp_uid, token] = SlippageEstimator(self.window_size, self.quantization, block)
        estimator = self.estimators[lp_uid, token]
        r = estimator.estimate_signal(block)
        if r is None:
            logger.debug(f"LP {lp_uid} has no slippage information yet, since only {len(estimator.observations)}/{estimator.window_size} observations were collected.")
        return r

    def estimate_signals(self, lp_uid: str, block: int, tokens: list[Token]) -> Optional[float]:
        r = {token: self.estimate_signal(lp_uid=lp_uid, token=token, block=block) for token in tokens}
        r = {k: v for k, v in r.items() if v is not None}
        if len(r) == 0:
            return None
        return r

    def initialize(self, lp_uid: str, block: int, tokens: list[Token]):
        for token in tokens:
            if (lp_uid, token) not in self.estimators:
                self.estimators[lp_uid, token] = SlippageEstimator(self.window_size, self.quantization, block)

    def debug(self, block):
        for (lp_uid, t), e in self.estimators.items():
            estimate = self.estimate(lp_uid, t, block, 0.05)
            estimate_dec = estimate*10**-t.decimals if estimate is not None else None
            print(lp_uid, t.symbol, len(e.observations), estimate_dec)
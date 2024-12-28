

import datetime
from itertools import permutations
import math
from typing import Callable, Iterable, Optional, Tuple
from lpbook.util import LP, Token, Trade

class LinearRegression:
    def __init__(self, x_train: Iterable[int], y_train: Iterable[float]):
        self.x_train = list(x_train)
        self.y_train = list(y_train)
        n = len(self.x_train)
        assert n == len(self.y_train)
        assert n >= 2
        if len(set(self.y_train)) == 1:
            self.slope = 0
            self.intercept = self.y_train[0]
            return
        sum_x = sum(self.x_train)
        sum_y = sum(self.y_train)
        sum_x2 = sum(x**2 for x in self.x_train)
        sum_xy = sum(x * y for x, y in zip(self.x_train, self.y_train))
        self.slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
        self.intercept = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)

    def __call__(self, x: int) -> float:
        return self.slope * x + self.intercept

    def stderr_of_residuals(self) -> Optional[float]:
        r2 = [(self(x) - y_observed)**2 for x, y_observed in zip(self.x_train, self.y_train)]
        if len(r2) <= 2:
            return None
        return math.sqrt(sum(r2) / (len(r2) - 2))


class LogLinearRegression:
    def __init__(self, x_train: Iterable[int], y_train: Iterable[float]):
        self.x_train = list(x_train)
        self.log_y_train = [math.log(y) for y in y_train]
        n = len(self.x_train)
        assert n == len(self.log_y_train)
        assert n >= 2
        if len(set(self.log_y_train)) == 1:
            self.slope = 0
            self.intercept = self.log_y_train[0]
            return
        sum_x = sum(self.x_train)
        sum_y = sum(self.log_y_train)
        sum_x2 = sum(x**2 for x in self.x_train)
        sum_xy = sum(x * y for x, y in zip(self.x_train, self.log_y_train))
        self.slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
        self.intercept = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)

    def __call__(self, x: int) -> float:
        return math.exp(self.slope * x + self.intercept)

    def stderr_of_residuals(self) -> Optional[float]:
        r2 = [(math.log(self(x)) - y_observed)**2 for x, y_observed in zip(self.x_train, self.log_y_train)]
        if len(r2) <= 2:
            return None
        return math.sqrt(sum(r2) / (len(r2) - 2))


def make_regression_with_uncertainty(R):
    class RegressionWithUncertainty(R):
        def estimate_of_average(self, from_block: int, to_block: int) -> float:
            return (self(to_block) + self(from_block)) / 2

        def stddev_of_estimate_of_average(self, from_block: int, to_block: int) -> Optional[float]:
            sigma = self.stderr_of_residuals()
            if sigma is None:
                return None
            n = len(self.x_train)
            m = to_block - from_block + 1
            mean_x = sum(self.x_train) / n
            sum_sd_x = sum((x - mean_x) ** 2 for x in self.x_train)
            
            t1 = (m + 1) * (2 * from_block + m  - 2 * mean_x) / 2
            r = math.sqrt((sigma / m) ** 2  * ((m+1)**2 / n + t1 ** 2 / sum_sd_x))
            return r

    return RegressionWithUncertainty


class TradedAmountsCollector:
    def __init__(self, token1: Token, token2: Token,  window_size: int, block: int, last_xrate12: Optional[float] = None):
        self.token1 = token1
        self.token2 = token2
        self.window_size = window_size
        self.last_block = block
        self.abs_amounts1 = [0] # abs_amounts1 is the traded amount of token1 (absolute value)
        self.abs_amounts2 = [0]
        self.last_xrates12 = [last_xrate12]

    def record_trade(self, block: int, buy_amount1: int, buy_amount2: int):
        if block > self.last_block:
            for x in [self.abs_amounts1, self.abs_amounts2]:
                x += [0] * (block - self.last_block)
            self.last_xrates12 += [self.last_xrates12[-1]] * (block - self.last_block)
            self.last_block = block
        assert block <= self.last_block
        self.abs_amounts1[block - self.last_block - 1] += abs(buy_amount1)
        self.abs_amounts2[block - self.last_block - 1] += abs(buy_amount2)
        if self.abs_amounts1[block - self.last_block - 1] != 0 and self.abs_amounts2[block - self.last_block - 1] != 0:
            self.last_xrates12[block - self.last_block - 1] = self.abs_amounts2[block - self.last_block - 1] / self.abs_amounts1[block - self.last_block - 1]
        for x in [self.abs_amounts1, self.abs_amounts2, self.last_xrates12]:
            if len(x) > 2*self.window_size:
                x = x[-self.window_size:]

    # p(t1) / p(t2)
    def xrate12(self, block) -> Optional[float]:
        n_observations = len(self.last_xrates12)
        assert self.last_block - n_observations + 1 <= block <= self.last_block
        return self.last_xrates12[block - self.last_block - 1]

    def xrates12(self, from_block: int, to_block: int) -> list[Optional[float]]:
        return [self.xrate12(block) for block in range(from_block, to_block + 1)]
        
    # E(p(t1) / p(t2))
    def average_xrate12(self, from_block: int, to_block: int) -> Optional[float]:
        r = [self.xrate12(block) for block in range(from_block, to_block + 1)]
        r = [x for x in r if x is not None]
        return sum(r) / len(r) if len(r) > 0 else None
    
    # Linear regression of xrate12 over the interval [from_block, to_block]
    def regress_xrate12(self, from_block: int, to_block: int) -> Optional[Callable[[int], float]]:
        n_observations = len(self.abs_amounts1)
        assert self.last_block - n_observations + 1 <= from_block <= to_block <= self.last_block
        x = []
        y = []
        for block in range(from_block , self.last_block + 1):
            xrate12 = self.xrate12(block)
            if xrate12 is not None:
                x.append(block)
                y.append(xrate12)
        if len(x) < 2:
            return None
        return make_regression_with_uncertainty(LogLinearRegression)(x, y)

    def estimate_average_xrate12_in_running_hour(self, block: int, block_time: datetime.datetime) -> Tuple[Optional[float], Optional[float]]:
        self.record_trade(block, 0, 0)
        if  len(self.last_xrates12) < self.window_size:
            return None, None

        start_of_hour = block_time.replace(minute=0, second=0, microsecond=0)
        nr_observations_since_start_of_hour = math.floor((block_time - start_of_hour).total_seconds() / 12)
        nr_observations_in_time_window = sum(self.xrate12(block - i) is not None for i in range(self.window_size))
        nr_observations = min(nr_observations_since_start_of_hour, nr_observations_in_time_window)

        first_block_observed = block - nr_observations + 1
        observed_avg_xrate12 = self.average_xrate12(first_block_observed, block)

        nr_estimates = 3600//12 - nr_observations_since_start_of_hour
        if nr_estimates == 0:
            return observed_avg_xrate12, 0

        first_block_for_training = block - self.window_size + 1
        xrate_predictor = self.regress_xrate12(first_block_for_training, block)
        if xrate_predictor is None:
            return None, None
           
        last_block_of_hour = block + nr_estimates
        predicted_avg_xrate12 = xrate_predictor.estimate_of_average(block + 1, last_block_of_hour) 
        
        assert predicted_avg_xrate12 is not None
        
        if observed_avg_xrate12 is None:
            assert nr_observations == 0
            observed_avg_xrate12 = 0  # since it cancels out in the weighted average below

        estimate = (
            (observed_avg_xrate12 * nr_observations + predicted_avg_xrate12 * nr_estimates) / 
            (nr_observations + nr_estimates)
        )

        stddev_of_estimate_of_average = xrate_predictor.stddev_of_estimate_of_average(self.last_block + 1, last_block_of_hour)
        if stddev_of_estimate_of_average is None:
            return estimate, None

        stddev = (
            (0 * nr_observations + stddev_of_estimate_of_average * nr_estimates)  / 
            (nr_observations + nr_estimates)
        )

        #print("tokens: ", self.token1.symbol, self.token2.symbol)
        #print("observations: ", [x for x in self.xrates12(first_block_observed, block) if x is not None])
        #print("training:", [x for x in self.xrates12(first_block_for_training, block) if x is not None])
        #print(f"nr_observations_since_start_of_hour: {nr_observations_since_start_of_hour}")
        #print(f"nr_observations: {nr_observations}")
        #print(f"nr_estimates: {nr_estimates}")
        #print(f"observed_avg_xrate12: {observed_avg_xrate12}")
        #print(f"predicted_avg_xrate12: {predicted_avg_xrate12}")
        #print(f"slope: {xrate_predictor.slope}")
        #print(f"intercept: {xrate_predictor.intercept}")
        #print(f"estimate: {estimate}")
        #print(f"stddev_of_estimate_of_average: {stddev_of_estimate_of_average}")
        #print(f"stddev: {stddev}")

        return estimate, stddev


class TradedAmountsCollectors:
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.collectors = {}

    def record_buy_amount(self, block: int, token1: Token, token2: Token, buy_amount1: int, buy_amount2: int):
        if (token1, token2) not in self.collectors:
            self.collectors[token1, token2] = TradedAmountsCollector(token1, token2, self.window_size, block)
        self.collectors[token1, token2].record_trade(block, buy_amount1, buy_amount2)

    def record_trade(self, trade: Trade):
        self.record_buy_amount(block=trade.block_number, token1=trade.token1, token2=trade.token2, buy_amount1=trade.buy_amount1, buy_amount2=trade.buy_amount2)
        self.record_buy_amount(block=trade.block_number, token1=trade.token2, token2=trade.token1, buy_amount1=trade.buy_amount2, buy_amount2=trade.buy_amount1)

    def initialize(self, lp: LP, block: int):
        spot_xrates = lp.spot_xrates
        for token1, token2 in permutations(lp.tokens, 2):            
            if (token1, token2) not in self.collectors:
                xrate12 = spot_xrates[token1, token2].p_buy_over_p_sell if (token1, token2) in spot_xrates else None
                self.collectors[token1, token2] = TradedAmountsCollector(token1, token2, self.window_size, block, xrate12)
    
    def estimate_average_xrates_in_running_hour(self, token_pairs: Iterable[Tuple[Token, Token]], block_number: int, block_time: datetime.datetime) -> dict[Tuple[Token, Token], Tuple[float, Optional[float]]]:
        r = {}
        for token1, token2 in token_pairs:
            if (token1, token2) not in self.collectors:
                continue
            xrate, stderr = self.collectors[token1, token2].estimate_average_xrate12_in_running_hour(block_number, block_time)
            if xrate is not None:
                r[token1, token2] = xrate, stderr
        return r
    
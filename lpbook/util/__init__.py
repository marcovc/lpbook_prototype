from abc import abstractproperty
import asyncio
from contextlib import contextmanager
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import List, Dict, Optional, Tuple

import functools
import time

from lpbook.web3 import BlockId


# possible values for clocks:
# time.perf_counter - does not stop during sleep
# time.process_time - stops during sleep
@contextmanager
def traced_context(logger, description, include_cpu_bound_only=False):
    start_time = time.perf_counter()
    if include_cpu_bound_only:
        start_time_cpu = time.process_time()
    logger.debug(f'{description} ...')
    yield
    end_time = time.perf_counter()
    run_time = end_time - start_time
    if include_cpu_bound_only:
        end_time_cpu = time.process_time()
        run_time_cpu = end_time_cpu - start_time_cpu
        logger.debug(f'{description} ... done ({run_time:.4f} secs, {run_time_cpu:.4f} CPU secs)')
    else:
        logger.debug(f'{description} ... done ({run_time:.4f} secs)')

def traced(logger, description=None):
    """Logs calls to the decorated function."""
    def traced_decorator(func):
        nonlocal description
        if description is None:
            description = f'{func.__name__!r}'

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            with traced_context(logger, description):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    logger.error(f'Caught exception in {func.__name__!r}: {err}')
                    raise

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            with traced_context(logger, description):
                try:
                    return await func(*args, **kwargs)
                except Exception as err:
                    logger.error(f'Caught exception in {func.__name__!r}: {err}')
                    raise

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return traced_decorator


@dataclass
class Token:
    address: str
    symbol: str
    decimals: int

    def __hash__(self):
        return self.address.__hash__()

        
# Recursively convert an object to a dict
# https://stackoverflow.com/questions/1036409/recursively-convert-python-object-graph-to-dictionary
def to_dict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = to_dict(v, classkey)
        return data
    elif hasattr(obj, '_ast'):
        return to_dict(obj._ast())
    elif hasattr(obj, '__iter__') and not isinstance(obj, str):
        return [to_dict(v, classkey) for v in obj]
    elif hasattr(obj, '__dict__'):
        data = dict([
            (key, to_dict(value, classkey))
            for key, value in obj.__dict__.items()
            if not callable(value) and not key.startswith('_')
        ])
        if classkey is not None and hasattr(obj, '__class__'):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


# Recursively wrap all numbers as string.
def stringify_numbers(obj, except_keys):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            if k not in except_keys:
                data[stringify_numbers(k, except_keys)] = stringify_numbers(v, except_keys)
            else:
                data[k] = v
        return data
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, float) or isinstance(obj, int) or isinstance(obj, Decimal) or isinstance(obj, Fraction):
        return str(obj)
    elif isinstance(obj, list):
        return [stringify_numbers(element, except_keys) for element in obj]
    elif obj is None:
        return None
    else:
        raise NotImplementedError(f"Can't stringify {obj}.")

@dataclass
class ExchangeRate:
    buy_token: Token
    sell_token: Token
    p_buy_over_p_sell: float
        
@dataclass
class LP:
    @abstractproperty
    def uid(self) -> str:
        """Returns a unique identifier for the LP (like its address)."""

    @abstractproperty
    def kind(self) -> str:
        """Returns the kind of the LP (ConstProd, Concentrated, etc.)."""

    @abstractproperty
    def protocol_name(self) -> str:
        """Returns the name of lp protocol (Uniswap, Curve, etc.)."""

    @abstractproperty
    def protocol_version(self) -> str:
        """Returns the version of lp protocol."""

    @property
    def protocol(self) -> str:
        """Returns the name and version of the lp protocol."""
        return f'{self.protocol_name}_{self.protocol_version}'
    
    @abstractproperty
    def tokens(self) -> List[Token]:
        """Returns a list of tokens pooled by this LP."""

    @abstractproperty
    def state(self) -> Dict:
        """Returns the internal state of the LP (e.g. the two reserves for uniswapV2)."""

    @abstractproperty
    def gas_stats(self) -> Dict:
        """Returns gas stats for swapping using this pool."""

    @property
    def execution_info(self) -> Dict:
        """Returns extra info for executing LPBook onchain."""
        return {}

    @abstractproperty
    def internalizable(self) -> bool:
        """Returns if this pool is allowed to be internalized."""

    @property
    def may_have_slippage(self) -> bool:
        return False

    @property
    def spot_xrates(self) -> dict[Tuple[Token, Token], ExchangeRate]:
        return {}
    
    #def estimate_slippage(self, lp_monitors, block_number, risk):
    #    self.slippage = lp_monitors.slippage_estimators.estimates(self.uid, block_number, tokens=self.tokens, risk=risk)

    #def estimate_signal(self, lp_monitors, block_number):
    #    self.signal = lp_monitors.slippage_estimators.estimate_signals(self.uid, block_number, tokens=self.tokens)

    def marshall(self) -> Dict:
        """Encodes itself to a dict with a common API."""
        api = {
            'id': self.uid,
            'kind': self.kind,
            'tokens': self.tokens,
            'state': self.state,
            'gas_stats': self.gas_stats,
            'chain_info': {
                'protocol': self.protocol,
                'execution': self.execution_info
            }
        }

        if hasattr(self, "slippage") and self.slippage is not None: 
            slippage = {t.address: self.slippage[t] for t,s in self.slippage.items() if s is not None and s != 0}
            if len(slippage) > 0:
                api['slippage'] = slippage
        if hasattr(self, "signal") and self.signal is not None: 
            signal = {t.address: self.signal[t] for t,s in self.signal.items() if s is not None}
            if len(signal) > 0:
                api['signal'] = signal
        try:
            return stringify_numbers(to_dict(api), {'decimals'})
        except NotImplementedError:
            raise RuntimeError(f"Can't marshall LP {api}")

@dataclass
class Trade:
    lp_id: str
    block_number: int
    token1: Token
    token2: Token
    buy_amount1: int
    buy_amount2: int

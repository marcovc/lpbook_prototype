

from typing import Dict, List
from lpbook.util import LP, Token


class FixedRate(LP):
    # https://etherscan.io/address/0x3225737a9Bbb6473CB4a45b7244ACa2BeFdB276A#code
    def __init__(self, address, token1, token2, max_sell_amount1, max_sell_amount2, gas):
        self.address = address
        self.token1 = token1
        self.token2 = token2
        self.max_sell_amount1 = max_sell_amount1
        self.max_sell_amount2 = max_sell_amount2
        self.gas = gas

    @property
    def uid(self) -> str:
        """Returns a unique identifier for the LP (like its address)."""
        return self.address

    @classmethod
    @property
    def kind(self) -> str:
        return 'FixedRate'

    @classmethod
    @property
    def protocol_name(self) -> str:
        """Returns the name of lp protocol (Uniswap, Curve, etc.)."""
        return "FixedRate"

    @classmethod
    @property
    def protocol_version(self) -> str:
        """Returns the version of lp protocol."""
        return 1

    @property
    def tokens(self) -> List[Token]:
        """Returns a list of tokens pooled by this LP."""
        return [self.token1, self.token2]

    @property
    def state(self) -> Dict:
        """Returns the internal state of the LP (e.g. the two reserves for uniswapV2)."""
        return {
            "balances" : [self.max_sell_amount1, self.max_sell_amount2]
        }

    @property
    def gas_stats(self) -> Dict:
        """Returns gas stats for swapping using this pool."""
        return {
            'mean': self.gas,
            'stddev': 0,
        }


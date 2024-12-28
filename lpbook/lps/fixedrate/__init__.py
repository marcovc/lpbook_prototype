
from typing import Dict, List

from lpbook import (LPDriver,
                    LPSyncProxy)
from lpbook.util import LP, Token
from lpbook.web3 import BlockId


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


class IdenditySyncProxy(LPSyncProxy):
    def __init__(self, lps):
        self.lps = {lp.uid: lp for lp in lps}

    def __call__(self, block: BlockId) -> Dict[str, LP]:
        return self.lps

    async def start(self) -> None:
        pass

    def stop(self) -> None:
        pass


class FixedRateDriver(LPDriver):

    lps = [
        FixedRate(
            address="0x3225737a9Bbb6473CB4a45b7244ACa2BeFdB276A".lower(),
            token1=Token('0x6b175474e89094c44da98b954eedeac495271d0f'.lower(), 'DAI', 18),
            token2=Token('0xdC035D45d973E3EC169d2276DDab16f1e407384F'.lower(), 'USDS', 18),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e18),
            gas=145000,
        ),
        FixedRate(
            address="0xBDcFCA946b6CDd965f99a839e4435Bcdc1bc470B".lower(),
            token1=Token('0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'.lower(), 'MKR', 18),
            token2=Token('0x56072C95FAA701256059aa122697B133aDEd9279'.lower(), 'SKY', 18),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e18) * int(24000),
            gas=79500,
        ),
        FixedRate(
            address="0xf6e72db5454dd049d0788e411b06cfaf16853042".lower(),
            token1=Token('0x6b175474e89094c44da98b954eedeac495271d0f'.lower(), 'DAI', 18),
            token2=Token('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'.lower(), 'USDC', 6),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e6),
            gas=40000,
        ),
    ]

    def __init__(self):
        super().__init__(FixedRate)
        self.lp_by_uid = {lp.uid : lp for lp in self.lps}

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        """Collects addresses of lps involving given tokens."""
        token_ids = set(token_ids)
        return [
            lp.uid 
            for lp in self.lps
            if len({lp.token1.address, lp.token2.address}.intersection(token_ids)) == 2
        ]

    async def create_lp_sync_proxy(
        self, 
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        """Creates a new LPSyncProxy instance that tracks a set of lps."""
        lps = [
            self.lp_by_uid[lp_uid] for lp_uid in lp_ids
        ]
        return IdenditySyncProxy(lps)

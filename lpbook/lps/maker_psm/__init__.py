
from typing import Dict, List

from lpbook import (LPDriver,
                    LPSyncProxy)
from lpbook.util import LP, Token
from lpbook.web3 import BlockId


class MakerPSM(LP):
    # tin and tout are "toll in" and "toll out" - the fees
    # see https://github.com/makerdao/dss-psm/blob/master/src/psm.sol 
    def __init__(self, address, gem_join_address, gem_token, dai_token, tin, tout):
        self.address = address
        self.gem_join_address = gem_join_address
        self.gem_token = gem_token
        self.dai_token = dai_token
        self.tin = tin
        self.tout = tout

    @property
    def uid(self) -> str:
        """Returns a unique identifier for the LP (like its address)."""
        return self.address

    @classmethod
    @property
    def kind(self) -> str:
        return 'MakerPSM'

    @property
    def protocol_name(self) -> str:
        """Returns the name of lp protocol (Uniswap, Curve, etc.)."""
        return "MakerPSM"

    @property
    def protocol_version(self) -> str:
        """Returns the version of lp protocol."""
        return "1"

    @property
    def tokens(self) -> List[Token]:
        """Returns a list of tokens pooled by this LP."""
        return [self.gem_token, self.dai_token]

    @property
    def state(self) -> Dict:
        """Returns the internal state of the LP (e.g. the two reserves for uniswapV2)."""
        return {
            "gem_address": self.gem_token.address,
            "dai_address": self.dai_token.address,
            "gem_join_address": self.gem_join_address,
            "tin": self.tin,
            "tout": self.tout,
            "dai_balance": 100000000e18,  # can be read from usdc contract (.balanceOf(gem_join_address))
            "gem_balance": 100000000e6
        }

    @property
    def gas_stats(self) -> Dict:
        """Returns gas stats for swapping using this pool."""
        return {
            'nr_obs': 1487,
            'mean': 200792,
            'stddev': 18932.42393898834,
            'min': 14386,
            'max': 249147,
            'median': 202321
        }


class MakerPSMSyncProxy(LPSyncProxy):
    def __init__(self, lps):
        self.lps = {lp.uid: lp for lp in lps}

    def __call__(self, block: BlockId) -> Dict[str, LP]:
        return self.lps

    async def start(self) -> None:
        pass

    def stop(self) -> None:
        pass


class MakerPSMDriver(LPDriver):
    USDC = Token('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'USDC', 6)
    DAI = Token('0x6b175474e89094c44da98b954eedeac495271d0f', 'DAI', 18)

    USDC_DAI = "0x89b78cfa322f6c5de0abceecab66aee45393cc5a"
    USDC_JOIN = "0x0a59649758aa4d66e25f08dd01271e891fe52199"

    def __init__(self):
        super().__init__(MakerPSM)

    async def get_lp_ids(self, token_ids: List[str]) -> List[str]:
        """Collects addresses of lps involving given tokens."""
        def is_valid_token(token):
            return token in [
                self.USDC.address,
                self.DAI.address
            ]

        if sum(is_valid_token(t) for t in token_ids) == 2:
            return [self.USDC_DAI]
        else:
            return []

    async def create_lp_sync_proxy(
        self, 
        lp_ids: List[str],
        data_source: LPDriver.LPSyncProxyDataSource =
            LPDriver.LPSyncProxyDataSource.Default
    ) -> LPSyncProxy:
        """Creates a new LPSyncProxy instance that tracks a set of lps."""
        lps = []
        if self.USDC_DAI in lp_ids:
            lps.append(MakerPSM(self.USDC_DAI, self.USDC_JOIN, self.USDC, self.DAI, 0, 0))

        return MakerPSMSyncProxy(lps)

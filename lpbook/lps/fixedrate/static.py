
from typing import Dict, List
from lpbook import LPDriver, LPSyncProxy
from lpbook.lps.fixedrate.FixedRate import FixedRate
from lpbook.util import LP, Token
from lpbook.web3 import BlockId
from lpbook.web3.block_stream import BlockStream

class StaticFixedRate(FixedRate):
    @classmethod
    @property
    def protocol_name(self) -> str:
        """Returns the name of lp protocol (Uniswap, Curve, etc.)."""
        return "StaticFixedRate"

    @classmethod
    @property
    def protocol_version(self) -> str:
        """Returns the version of lp protocol."""
        return 1

class IdenditySyncProxy(LPSyncProxy):
    def __init__(self, lps, block_stream: BlockStream):
        self.lps = {lp.uid: lp for lp in lps}
        self.on_sync_subscribers = []
        self.block_stream = block_stream

    def __del__(self):
        self.block_stream.unsubscribe(self.on_new_block)

    def subscribe_on_sync(self, subscriber):
        self.on_sync_subscribers.append(subscriber)

    def unsubscribe_on_sync(self, subscriber):
        self.on_sync_subscribers = [s for s in self.on_sync_subscribers if s != subscriber]

    async def on_new_block(self, block: BlockId):
        for subscriber in self.on_sync_subscribers:
            subscriber(block, self)

    def __call__(self, block: BlockId) -> Dict[str, LP]:
        return self.lps

    async def start(self) -> None:
        self.block_stream.subscribe(self.on_new_block)


    async def stop(self) -> None:
        self.block_stream.unsubscribe(self.on_new_block)



class StaticFixedRateDriver(LPDriver):

    lps = [
        StaticFixedRate(
            address="0x3225737a9Bbb6473CB4a45b7244ACa2BeFdB276A".lower(),
            token1=Token('0x6b175474e89094c44da98b954eedeac495271d0f'.lower(), 'DAI', 18),
            token2=Token('0xdC035D45d973E3EC169d2276DDab16f1e407384F'.lower(), 'USDS', 18),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e18),
            gas=145000,
        ),
        StaticFixedRate(
            address="0xBDcFCA946b6CDd965f99a839e4435Bcdc1bc470B".lower(),
            token1=Token('0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'.lower(), 'MKR', 18),
            token2=Token('0x56072C95FAA701256059aa122697B133aDEd9279'.lower(), 'SKY', 18),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e18) * int(24000),
            gas=79500,
        ),
        StaticFixedRate(
            address="0xf6e72db5454dd049d0788e411b06cfaf16853042".lower(),
            token1=Token('0x6b175474e89094c44da98b954eedeac495271d0f'.lower(), 'DAI', 18),
            token2=Token('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'.lower(), 'USDC', 6),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e6),
            gas=40000,
        ),
        StaticFixedRate(
            address="0xA188EEC8F81263234dA3622A406892F3D630f98c".lower(),
            token1=Token('0xdC035D45d973E3EC169d2276DDab16f1e407384F'.lower(), 'USDS', 18),
            token2=Token('0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'.lower(), 'USDC', 6),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e6),
            gas=40000,
        ),
        StaticFixedRate(
            address="0x4d5F47FA6A74757f35C14fD3a6Ef8E3C9BC514E8".lower(),
            token1=Token('0x4d5F47FA6A74757f35C14fD3a6Ef8E3C9BC514E8'.lower(), 'aEthWETH', 18),
            token2=Token('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'.lower(), 'WETH', 18),
            max_sell_amount1=int(100000000e18),
            max_sell_amount2=int(100000000e18),
            gas=150000,
        )
    ]

    def __init__(self, block_stream: BlockStream):
        super().__init__(StaticFixedRate)
        self.lp_by_uid = {lp.uid : lp for lp in self.lps}
        self.block_stream = block_stream

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
        return IdenditySyncProxy(lps, self.block_stream)

    @property
    def uid(self) -> str:
        return f"{self.protocol}-{self.kind}"

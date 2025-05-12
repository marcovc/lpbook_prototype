
import os
from typing import Optional

from dotenv import load_dotenv
from lpbook.lps.uniswap_v3.common import UniV3Like, UniV3LikeDriver, UniV3LikeTheGraphAndWeb3Proxy, UniV3LikeTheGraphProxy
from lpbook.web3 import BlockId

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")


class PancakeswapV3(UniV3Like):
    """Pancakeswap V3 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Pancakeswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'


UniV3Like.as_pancakeswapv3 = lambda self: PancakeswapV3(**self.__dict__)


class PancakeSwapV3TheGraphProxy(UniV3LikeTheGraphProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[PancakeswapV3]:
        univ3_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ3_like is None:
            return None
        return univ3_like.as_pancakeswapv3()



class PancakeswapV3Driver(UniV3LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/pancakeswap/exchange-v3-eth'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/CJYGNhb7RvnhfBDjqpRnD3oxgyhibzc7fkAMa38YV3oS'
        self.UniV3Like = PancakeswapV3
        self.UniV3LikeTheGraphProxy = PancakeSwapV3TheGraphProxy
        self.UniV3LikeTheGraphAndWeb3Proxy = UniV3LikeTheGraphAndWeb3Proxy
        self.abi_filename = 'pancakeswap_v3.abi'
        super().__init__(*args, **kwargs)
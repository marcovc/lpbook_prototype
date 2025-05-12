
import os
from typing import Optional

from dotenv import load_dotenv
from lpbook.lps.uniswap_v3.common import UniV3Like, UniV3LikeDriver, UniV3LikeTheGraphAndWeb3Proxy, UniV3LikeTheGraphProxy
from lpbook.web3 import BlockId

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")


class UniV3(UniV3Like):
    """Uniswap V3 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Uniswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'


UniV3Like.as_univ3 = lambda self: UniV3(**self.__dict__)

class UniV3TheGraphProxy(UniV3LikeTheGraphProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[UniV3]:
        univ3_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ3_like is None:
            return None
        return univ3_like.as_univ3()

class UniV3Driver(UniV3LikeDriver):
    def __init__(self, *args, **kwargs):
        #self.thegraph_url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV'
        self.UniV3Like = UniV3
        self.UniV3LikeTheGraphProxy = UniV3TheGraphProxy
        self.UniV3LikeTheGraphAndWeb3Proxy = UniV3LikeTheGraphAndWeb3Proxy
        self.abi_filename = 'uniswap_v3.abi'
        super().__init__(*args, **kwargs)

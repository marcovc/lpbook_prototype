
import os
from typing import Optional

from dotenv import load_dotenv
from lpbook.lps.uniswap_v3.common import UniV3Like, UniV3LikeDriver, UniV3LikeTheGraphAndWeb3Proxy, UniV3LikeTheGraphProxy
from lpbook.web3 import BlockId

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")


class SolidlyV3(UniV3Like):
    """Solidly V3 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Solidly'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '3'


UniV3Like.as_solidlyv3 = lambda self: SolidlyV3(**self.__dict__)



class SolidlyV3TheGraphProxy(UniV3LikeTheGraphProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[SolidlyV3]:
        univ3_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ3_like is None:
            return None
        return univ3_like.as_solidlyv3()




class SolidlyV3Driver(UniV3LikeDriver):
    def __init__(self, *args, **kwargs):
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/7StqFFqbxi3jcN5C9YxhRiTxQM8HA8XEHopsynqqxw3t'
        self.UniV3Like = SolidlyV3
        self.UniV3LikeTheGraphProxy = SolidlyV3TheGraphProxy
        self.UniV3LikeTheGraphAndWeb3Proxy = UniV3LikeTheGraphAndWeb3Proxy
        self.abi_filename = 'solidly_v3.abi'
        super().__init__(*args, **kwargs)

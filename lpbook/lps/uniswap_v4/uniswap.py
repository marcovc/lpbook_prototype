
import os
from typing import Dict, Optional

from dotenv import load_dotenv
from lpbook.lps.uniswap_v4.common import UniV4Like, UniV4LikeDriver, UniV4LikeTheGraphAndWeb3Proxy, UniV4LikeTheGraphProxy
from lpbook.web3 import BlockId

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")

POOL_MANAGER_ADDRESS = '0x000000000004444c5dc75cb358380d2e3de08a90'
PERMIT2_ADDRESS = '0x000000000022d473030f116ddee9f6b43ac78ba3'
ROUTER_ADDRESS = '0x66a9893cc07d91d95644aedd05d03f95e1dba8af'

class UniV4(UniV4Like):
    """Uniswap V4 LP."""
    @classmethod
    @property
    def protocol_name(self) -> str:
        return 'Uniswap'

    @classmethod
    @property
    def protocol_version(self) -> str:
        return '4'

    @property
    def execution_info(self) -> Dict:
        base_info = super().execution_info
        base_info.update({
            'pool_manager': POOL_MANAGER_ADDRESS,
            'permit2': PERMIT2_ADDRESS,
            'router': ROUTER_ADDRESS,
        })
        return base_info

UniV4Like.as_univ4 = lambda self: UniV4(**self.__dict__)

class UniV4TheGraphProxy(UniV4LikeTheGraphProxy):
    def create_from_thegraph(self, thegraph_data, block: BlockId) -> Optional[UniV4]:
        univ4_like = super().create_from_thegraph(thegraph_data, block=block)
        if univ4_like is None:
            return None
        return univ4_like.as_univ4()

class UniV4Driver(UniV4LikeDriver):
    def __init__(self, *args, **kwargs):
        self.thegraph_url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/DiYPVdygkfjDWhbxGSqAQxwBKmfKnkWQojqeM2rkLb3G'
        self.UniV4Like = UniV4
        self.UniV4LikeTheGraphProxy = UniV4TheGraphProxy
        self.UniV4LikeTheGraphAndWeb3Proxy = UniV4LikeTheGraphAndWeb3Proxy
        self.abi_filename = 'uniswap_v4.abi'
        self.pool_manager = POOL_MANAGER_ADDRESS
        super().__init__(*args, **kwargs)

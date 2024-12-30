from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Union
from hexbytes import HexBytes

def get_erc20_contract(address: Optional[str], web3_client):
    with open(Path(__file__).parent / 'artifacts' / 'erc20.abi', 'r') as f:
        erc20_contract_abi = f.read()
    if address is not None:
        ERC20 = web3_client.eth.contract(abi=erc20_contract_abi, address=web3_client.to_checksum_address(address))
    else:
        ERC20 = web3_client.eth.contract(abi=erc20_contract_abi)
    return ERC20

async def create_token_from_web3(address, web3_client):
    from ..util import Token

    erc20 = get_erc20_contract(address=address, web3_client=web3_client)

    symbol = await erc20.functions.symbol().call()
    decimals = await erc20.functions.decimals().call()

    return Token(address=address.lower(), symbol=symbol, decimals=decimals)


@dataclass
class BlockId:
    """Identifies a block.

    If both number and hash are None, then it identifies the latest block.
    """

    number: Optional[int] = None
    hash: Optional[HexBytes] = None
    timestamp: Optional[int] = None

    def __hash__(self):
        return int.from_bytes(self.hash, byteorder="big")

    @classmethod
    def latest(cls):
        return BlockId(number=None, hash=None)

    def is_fully_qualified(self):
        return self.number is not None and self.hash is not None

    def with_number(self, number: int):
        return BlockId(hash=self.hash, number=number, timestamp=self.timestamp)

    def __str__(self) -> str:
        if self.number is None and self.hash is None:
            return '<latest>'
        elif self.number is not None and self.hash is not None:
            return f'{self.number}/{self.hash.hex()[:8]}'
        elif self.hash is not None:
            return self.hash.hex()[:8]
        else:
            return str(self.number)

    def datetime(self):
        return datetime.fromtimestamp(self.timestamp)
    
    @classmethod
    def from_web3(cls, block) -> "BlockId":
        return BlockId(number=block.number, hash=block.hash, timestamp=block.timestamp)

    def to_web3(self) -> str:
        if self.hash is not None:
            return self.hash
        elif self.number is not None:
            return self.number
        else:
            return 'latest'

    def to_thegraph_filter(self) -> Dict:
        block = {}
        if self.hash is not None:
            block.update(hash=self.hash.to_0x_hex())
        elif self.number is not None:
            block.update(number=self.number)
        if len(block) > 0:
            return {'block': block}
        return {}

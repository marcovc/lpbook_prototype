
from dataclasses import dataclass
from typing import Any, Optional
from pydantic import BaseModel

class LPExecution(BaseModel):
    lp_id: str
    protocol: str
    prev_block_hash: str
    target: str
    value: str
    calldata: str
    buy_amount: str
    buy_token_address: str
    sell_amount: str
    sell_token_address: str
    approved_spender: str
    auction_id: str
    simulated_gas: Optional[str]
    
    @property
    def short_name(self):
        return f"{self.protocol}_{self.buy_token_address[:6]}-{self.sell_token_address[:6]}"
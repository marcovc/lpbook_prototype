

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

from lpbook import LPFromInitialStatePlusChangesProxy
from lpbook.util import LP, Token


@dataclass
class COWAMM(LP):
    """Cow AMM."""
    lp: LP

    @property
    def tokens(self) -> List[Token]:
        return self.lp.tokens

    @property
    def uid(self) -> str:
        return self.lp.uid #self.owner.lower()

    @property
    def state(self) -> Dict:
        return {
            "state": self.lp.state,
            "kind": self.lp.kind,
            "protocol": self.lp.protocol,
        }

    @classmethod
    @property
    def kind(self) -> str:
        return 'COWAMM'




# It turns out COWBalancer pools don't emit swap events, so we use the Trade event emitted by
# the settlement contract, and filter out events that don't correspond to COWAMM pools.
# The downside of this approach, is that whenever there are deposits/withdrawals from
# the pool itself, the proxy balances will be out of sync, and will require a reset
# to catch up (i.e. reading the full pool state using an ASync proxy). 
class COWSwapWeb3Proxy(LPFromInitialStatePlusChangesProxy):
    """Queries Web3 for an initial state and for state updates."""
    SETTLEMENT_ADDRESS = "0x9008d19f58aabd9ed0d60971565aa8510560ab41"

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / 'COWSettlement.abi', 'r') as f:
            contract_abi = f.read()
        COW = web3_client.eth.contract(abi=contract_abi)
        super().__init__(
            [self.SETTLEMENT_ADDRESS],
            [COW.events.Trade],
            async_proxy,
            event_stream,
            web3_client
        )
        self.real_lp_ids = set(lp_ids)

    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""

        lp_id = d.args.owner.lower()
        if lp_id not in self.real_lp_ids:
            return
        assert lp_id in state.keys()
        lp = state[lp_id]

        assert d.event == 'Trade'
        token_in_address = d.args.buyToken.lower()
        token_out_address = d.args.sellToken.lower()

        token_in_index = [t.address == token_in_address for t in lp.tokens].index(True)
        token_out_index = [t.address == token_out_address for t in lp.tokens].index(True)

        lp.lp.balances[token_in_index] += d.args.buyAmount
        lp.lp.balances[token_out_index] -= d.args.sellAmount

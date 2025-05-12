
from pathlib import Path
from typing import Any, Dict, List, Tuple
from lpbook import LPFromInitialStatePlusChangesProxy
from lpbook.util import LP, Trade


class BalancerV3BalancesAndFeesWeb3SyncProxy(LPFromInitialStatePlusChangesProxy):
    # this the only contract that emits swap events (for all pools)
    BALANCER_VAULT_CONTRACT_ADDRESS="0xbA1333333333a1BA1108E8412f11850A5C319bA9"

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / 'Vault.abi', 'r') as f:
            contract_abi = f.read()
        Vault = web3_client.eth.contract(abi=contract_abi)

        self.lp_ids = lp_ids

        from eth_utils import to_hex, to_bytes
        topics = [
            to_hex(to_bytes(hexstr=address).rjust(32, b'\x00')) for address in self.lp_ids
        ]
        print(topics)
        super().__init__(
            [self.BALANCER_VAULT_CONTRACT_ADDRESS],
            [Vault.events.Swap, Vault.events.LiquidityAdded, Vault.events.LiquidityRemoved, Vault.events.AggregateSwapFeePercentageChanged],
            async_proxy,
            event_stream,
            web3_client,
            extra_topics=(topics,)
        )
    
    def get_token_indexes_from_swap_event(self, event, lp: LP) -> Tuple[int, int]:
        token_in = event.args["tokenIn"].lower()
        token_out = event.args["tokenOut"].lower()

        token_in_index = [t.address == token_in for t in lp.all_tokens].index(True)
        token_out_index = [t.address == token_out for t in lp.all_tokens].index(True)

        return token_in_index, token_out_index
    
    def get_token_indexes_from_balance_changed_event(self, event, lp: LP) -> List[int]:
        tokens = [token .lower() for token in event.args["tokens"]]
        token_indexes = []
        for token in tokens:
            token_index = [t.address == token for t in lp.all_tokens].index(True)
            token_indexes.append(token_index)
        return token_indexes
    
    def get_amounts_from_swap_event(self, event) -> Tuple[int, int]:
        amount_in = event.args["amountIn"]
        amount_out = event.args["amountOut"]
        return amount_in, amount_out
    
    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""
        lp_id = d.args["pool"]
        if lp_id not in state.keys():
            print("lp_id not in state.keys()")
            return
        lp = state[lp_id]
        if d.event == "Swap":
            token_in_index, token_out_index = self.get_token_indexes_from_swap_event(d, lp)
            amount_in, amount_out = self.get_amounts_from_swap_event(d)
            lp.balances[token_in_index] += amount_in
            lp.balances[token_out_index] -= amount_out
        elif d.event == "LiquidityAdded":
            for i, amount in enumerate(d.args["amountsAddedRaw"]):
                lp.balances[i] += amount
        elif d.event == "LiquidityRemoved":
            for i, amount in enumerate(d.args["amountsRemovedRaw"]):
                lp.balances[i] -= amount
        elif d.event == "AggregateSwapFeePercentageChanged":
            lp.fee_e18 = d.args["aggregateSwapFeePercentage"]

        print("updating state ", lp)

    def get_trades(self, cur_state: Dict[str, LP], changes: List[Any]) -> list[Trade]:
        """Assembles list of trades from updates."""
        r = []
        for d in changes:
            if d.event != "Swap":
                continue
            lp_id = d.args["pool"]
            if lp_id not in cur_state.keys():
                continue
            lp_cur_state = cur_state[lp_id]

            token_in_index, token_out_index = self.get_token_indexes_from_swap_event(d, lp_cur_state)
            amount_in, amount_out = self.get_amounts_from_swap_event(d)
                        
            r.append(
                Trade(
                    lp_id=lp_id, 
                    block_number=d.blockNumber, 
                    token1=lp_cur_state.all_tokens[token_in_index], 
                    token2=lp_cur_state.all_tokens[token_out_index],
                    buy_amount1=amount_in, 
                    buy_amount2=-amount_out
                )
            )
        return r

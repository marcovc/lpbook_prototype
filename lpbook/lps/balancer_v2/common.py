
from pathlib import Path
from typing import Any, Dict, List, Tuple
from lpbook import LPFromInitialStatePlusChangesProxy
from lpbook.util import LP, Trade


class BalancerV2BalancesWeb3SyncProxy(LPFromInitialStatePlusChangesProxy):
    # this the only contract that emits swap events (for all pools)
    BALANCER_VAULT_CONTRACT_ADDRESS="0xba12222222228d8ba445958a75a0704d566bf2c8"

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / 'Vault.abi', 'r') as f:
            contract_abi = f.read()
        Vault = web3_client.eth.contract(abi=contract_abi)

        lp_addresses = [self.get_lp_address_from_id(lp_id) for lp_id in lp_ids]
        self.lp_address_to_id = {
            lp_address: lp_id for lp_address, lp_id in zip(lp_addresses, lp_ids)
        }

        super().__init__(
            [self.BALANCER_VAULT_CONTRACT_ADDRESS],
            [Vault.events.Swap, Vault.events.PoolBalanceChanged],
            async_proxy,
            event_stream,
            web3_client
        )

    def get_lp_address_from_id(self, lp_id):
        return lp_id[:42]

    def get_lp_id_from_event(self, event):
        return f"0x{event.args['poolId'].hex().lower()}"
    
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
        lp_id = self.get_lp_id_from_event(d)
        if lp_id not in state.keys():
            return
        lp = state[lp_id]
        if d.event == "Swap":
            token_in_index, token_out_index = self.get_token_indexes_from_swap_event(d, lp)
            amount_in, amount_out = self.get_amounts_from_swap_event(d)
            lp.balances[token_in_index] += amount_in
            lp.balances[token_out_index] -= amount_out
        elif d.event == "PoolBalanceChanged":
            token_indexes = self.get_token_indexes_from_balance_changed_event(d, lp)
            deltas = d.args["deltas"]
            for i, delta in zip(token_indexes, deltas):
                lp.balances[i] += delta

        #print("updating state of ", lp_id, "from", prev_state[lp_id], "to", lp_cur_state, "@block", d.blockNumber)

    def get_trades(self, cur_state: Dict[str, LP], changes: List[Any]) -> list[Trade]:
        """Assembles list of trades from updates."""
        r = []
        for d in changes:
            if d.event != "Swap":
                continue
            lp_id = self.get_lp_id_from_event(d)
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



# The above does not emit events for Fee changes. Below proxy captures these.
class BalancerV2FeesWeb3SyncProxy(LPFromInitialStatePlusChangesProxy):
    # this the only contract that emits swap events (for all pools)

    def __init__(self, lp_ids, async_proxy, event_stream, web3_client):
        # read abi from same directory as this file.
        with open(Path(__file__).parent / 'artifacts' / 'WeightedPool.abi', 'r') as f:
            contract_abi = f.read()
        WeightedPool = web3_client.eth.contract(abi=contract_abi)

        lp_addresses = [self.get_lp_address_from_id(lp_id) for lp_id in lp_ids]
        #self.lp_address_to_id = {
        #    lp_address: lp_id for lp_address, lp_id in zip(lp_addresses, lp_ids)
        #}

        super().__init__(
            lp_addresses,
            [WeightedPool.events.SwapFeePercentageChanged],
            async_proxy,
            event_stream,
            web3_client
        )

    def get_lp_address_from_id(self, lp_id):
        return lp_id[:42]
            
    def update_state(self, state: Dict[str, LP], d: Any) -> None:
        """Assembles state from previous state and updates."""
        lp_id = d.address.lower()
        if lp_id not in state.keys():
            return
        lp = state[lp_id]
        assert d.event == "SwapFeePercentageChanged"
        lp.fee_e18 = d.event.args.swapFeePercentage



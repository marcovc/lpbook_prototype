from collections import namedtuple
from dataclasses import dataclass
import json
import logging
import os
from pathlib import Path
import pickle
from typing import List, Optional

import aiohttp

from .LPExecution import LPExecution
import requests
import web3
from dotenv import load_dotenv  

logger = logging.getLogger(__name__)

load_dotenv()

TENDERLY_ACCESS_KEY = os.getenv('TENDERLY_ACCESS_KEY')

UNISWAP_V3_CONTRACT_ADDRESS="0xe592427a0aece92de3edee1f18e0157c05861564"
WETH_ADDRESS="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"

tenderly_headers = {
    'X-Access-Key': TENDERLY_ACCESS_KEY,
    'Authorization': f'Bearer {TENDERLY_ACCESS_KEY}',
    'content-type': 'application/json',
}

@dataclass
class Transaction:
    from_: str
    to: str
    calldata: str
    state: Optional[dict] = None
    value: int = 0

def pad_left(hex_string):
    return f'0x{hex_string[2:]:>064}'

def to_hex256_string(i):
    return f'{i:#066x}'

# This works when both keys are addresses. 
def get_map_address_key_slot(map_slot, key1, key2=None):
    map_slot = f"{map_slot:064}"
    key1 = pad_left(key1)
    encoded_key1 =  web3.Web3.keccak(hexstr=key1 + map_slot).hex()
    if key2 is None:
        return encoded_key1
    key2 = pad_left(key2)
    encoded_key2 = web3.Web3.keccak(hexstr=key2 + encoded_key1[2:]).hex()
    return encoded_key2

UniV3Pool = namedtuple("UniV3Pool", ['id', 'fee_tier', 'tokens', 'tvl'])

async def get_univ3_pool_trading_tokens(token_address, token_addresses, http_client: aiohttp.ClientSession) -> Optional[UniV3Pool]:
    t = ",".join(f'"{token}"' for token in token_addresses)
    
    def parse_response(r):
        if 'data' not in r.keys():
            return None
        if 'pools' not in r['data'].keys():
            return None
        if len(r['data']['pools']) == 0:
            return None
        pool = r['data']['pools'][0]
        return UniV3Pool(
            id=pool['id'], 
            fee_tier=int(pool['feeTier']), 
            tokens=[pool['token0']['id'], pool['token1']['id']],
            tvl=[
                int(float(pool['totalValueLockedToken0'])*10**int(pool['token0']['decimals'])),
                int(float(pool['totalValueLockedToken1'])*10**int(pool['token1']['decimals']))
            ] 
        )
        
    query = '{pools(first:1, where:{token0:"' + token_address + '", token1_in:[' + t + '], liquidity_gt:"0"}, orderBy:totalValueLockedETH, orderDirection:desc){id feeTier totalValueLockedToken0 totalValueLockedToken1 token0 {id decimals} token1 {id decimals}}}'
    async with http_client.post(
        'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3',
        headers={'Content-Type': 'application/json'},
        json={'query': query}
    ) as r:
        r1 = parse_response(await r.json())

    query = '{pools(first:1, where:{token1:"' + token_address + '", token0_in:[' + t + '], liquidity_gt:"0"}, orderBy:totalValueLockedETH, orderDirection:desc){id feeTier totalValueLockedToken0 totalValueLockedToken1 token0 {id decimals} token1 {id decimals}}}'
    async with http_client.post(
        'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3',
        headers={'Content-Type': 'application/json'},
        json={'query': query}
    ) as r:
        r2 = parse_response(await r.json())
    if r1 is None:
        return r2
    if r2 is None:
        return r1
    if r1.tokens[0] == token_address:
        tvl1 = r1.tvl[0]
    else:
        tvl1 = r1.tvl[1]
    if r2.tokens[0] == token_address:
        tvl2 = r2.tvl[0]
    else:
        tvl2 = r2.tvl[1]
    if tvl1 > tvl2:
        return r1
    return r2

@dataclass
class Simulation:
    success: bool
    gas_used: Optional[int] = None
    error: Optional[str] = None
    tenderly_url: Optional[str] = None
    tenderly_simulation_data: Optional[dict] = None

class NoConnectionException(Exception):
    pass
class FailedBuyTransactionException(Exception):
    pass
class NoStateDiffException(Exception):
    pass

class Simulator:
    def __init__(self, web3_client, session: aiohttp.ClientSession, settlement_address: str):
        self.web3_client = web3_client
        self.http_client = session
        self.settlement_address = settlement_address
        with open(Path(__file__).parent / 'artifacts' / 'uniswap_v3.abi', 'r') as f:
            uniswap_v3_contract_abi = f.read()
        self.uniswap_v3_contract = web3_client.eth.contract(
            address=web3_client.to_checksum_address(UNISWAP_V3_CONTRACT_ADDRESS),
            abi=uniswap_v3_contract_abi
        )
        self.init_balance_keys()

    def get_balance_key(self, token_address) -> Optional[str]:
        if token_address in self.balance_keys:
            return self.balance_keys[token_address]
        elif token_address == WETH_ADDRESS:
            return get_map_address_key_slot(3, self.settlement_address)
        return None

    # sell_token_amount is a very large number by default, but not the max 2**256-1 (or near) because some tokens use last bits for encoding other things.
    def create_univ3_buy_token_transaction(self, fee_tier, buy_token_address, buy_token_amount, sell_token_address, sell_token_amount = 1 << 250) -> Transaction:
        sell_token_balance_key = self.get_balance_key(sell_token_address)
        assert sell_token_balance_key is not None
        calldata = self.uniswap_v3_contract.encodeABI(fn_name="exactOutputSingle", args=[(
            self.web3_client.to_checksum_address(sell_token_address),
            self.web3_client.to_checksum_address(buy_token_address),
            fee_tier,
            self.web3_client.to_checksum_address(self.settlement_address),
            2**256-1,
            buy_token_amount,
            sell_token_amount,
            0
        )])
        state = {
            sell_token_address: {
                sell_token_balance_key: to_hex256_string(sell_token_amount),
                #get_map_address_key_slot(4, UNISWAP_V3_CONTRACT_ADDRESS, self.settlement_address): to_hex256_string(WETH_BALANCE),
            }
        }
        return Transaction(from_=self.settlement_address, to=UNISWAP_V3_CONTRACT_ADDRESS, calldata=calldata, state=state)

    def create_lp_execution_transaction(self, lp_execution: LPExecution) -> Transaction:
        #state = {
        #    lp_execution.buy_token_address: {
        #        "storage": {
        #            get_map_address_key_slot(3, self.settlement_address): to_hex256_string(int(lp_execution.buy_amount)),
        #            get_map_address_key_slot(4, lp_execution.target, self.settlement_address): to_hex256_string(int(lp_execution.buy_amount)),
        #        }
        #    }
        #}
        return Transaction(from_=self.settlement_address, to=lp_execution.target, calldata=lp_execution.calldata)

    def tenderly_payload_from_transaction(self, transaction: Transaction, max_gas=4707788, block_number=None) -> dict:
        json_data = {
            'network_id': '1',
            'from': transaction.from_,
            'to': transaction.to,
            'input': transaction.calldata,
            'gas': max_gas,
            'value': str(transaction.value),
            'estimate_gas': True,
            'save_if_fails': True,
            'simulation_type': 'quick',
        }

        if transaction.state is not None:
            json_data["state_objects"] =  {k: {"storage": v} for k, v in transaction.state.items()}

        if block_number is not None:
            json_data["block_number"] = block_number

        return json_data

    async def simulate_transaction_via_tenderly(self, transaction: Transaction, max_gas=4707788, block_number=None) -> Simulation:
        json_data = self.tenderly_payload_from_transaction(transaction, max_gas, block_number)

        async with self.http_client.post(
            'https://api.tenderly.co/api/v1/account/marcovc/project/project/simulate',
            headers=tenderly_headers,
            json=json_data
        ) as r:
            r = await r.json()
            with open("last_tenderly_simulation.json", "w+") as f:  # TMP
                json.dump(r, f, indent=4)
            return Simulation(
                success=r["simulation"]["status"], 
                gas_used=r["simulation"]["gas_used"], 
                tenderly_url=f'https://dashboard.tenderly.co/marcovc/project/simulator/{r["simulation"]["id"]}',
                tenderly_simulation_data=r
            ) 


    async def simulate_transaction_via_web3(self, transaction: Transaction,  max_gas=4707788, block_number=None) -> Simulation:
        params = {
            "from": self.web3_client.to_checksum_address(transaction.from_),
            "to": self.web3_client.to_checksum_address(transaction.to),
            "data": transaction.calldata
        }                
        override_params = {k: {"stateDiff": v} for k, v in transaction.state.items()}
        try:
            await self.web3_client.eth.call(params, block_number if block_number is not None else "latest", override_params)
        except web3.exceptions.ContractLogicError as e:
            return Simulation(success=False, gas=None, error=e.message)
        return Simulation(success=True)

    async def get_connected_token_with_balance_key(self, token_address):
        pool = await get_univ3_pool_trading_tokens(token_address=token_address, token_addresses=self.balance_keys.keys(), http_client=self.http_client)
        if pool is None:
            return None, None, None
        if pool.tokens[0] == token_address:
            assert pool.tokens[1] in self.balance_keys
            return pool.tokens[1], pool.fee_tier, pool.tvl[0]
        else:
            assert pool.tokens[1] == token_address
            assert pool.tokens[0] in self.balance_keys
            return pool.tokens[0], pool.fee_tier, pool.tvl[1]

    # Try to guess balance key of a ERC20 contract.
    async def compute_balance_key(self, token_address: str) -> str:
        balance_key = self.get_balance_key(token_address)
        if balance_key is not None:
            return balance_key
        logger.debug(f"Cache miss for balance key for token {token_address}.")
        sell_token_address, univ3_fee_tier, tvl = await self.get_connected_token_with_balance_key(token_address)
        if sell_token_address is None:
            raise NoConnectionException(f"Could not infer balance key in ERC20 contract {token_address} since could not find a uni v3 pool connected to a token with a known balance key.")
        buy_amount = int(tvl / 10) # Use 1/10 of TVL of token for finding balance key. (TODO: use liquidity and sqrtprice from thegraph call to find what is the min amount we can buy)
        buy_transaction = self.create_univ3_buy_token_transaction(univ3_fee_tier, token_address, buy_amount, sell_token_address)
        simulation = await self.simulate_transaction_via_tenderly(buy_transaction)
        if not simulation.success:
            raise FailedBuyTransactionException(f"Could not infer balance key in ERC20 contract {token_address} since buy token transaction failed: {simulation.tenderly_url}")
        state_diff = simulation.tenderly_simulation_data["transaction"]["transaction_info"]["state_diff"]
        for diff in state_diff:
            if diff["address"] != token_address:
                continue
            d = diff["raw"][0]
            if int(d["dirty"], 16) == int(d["original"], 16) + buy_amount:
                key = d["key"]
                self.balance_keys[token_address] = key 
                self.save_balance_keys()
                return key
        raise NoStateDiffException(f"Could not infer balance key in ERC20 contract {token_address} since could not find any state diff.")

    def init_balance_keys(self):
        self.balance_keys = {}
        try:
            with open("balance_keys.pickle", "rb") as f:
                self.balance_keys = pickle.load(f)
        except Exception:
            logger.exception("Cound not load balance keys.")
            pass

    def save_balance_keys(self):
        with open("balance_keys.pickle", "wb+") as f:
            pickle.dump(self.balance_keys, f)
                
    async def get_balance_state_override(self, token_address: str, balance: int) -> dict:
        key = await self.compute_balance_key(token_address)
        return {token_address: {key: to_hex256_string(balance)}}

    async def simulate_execution(self, lp_execution: LPExecution, block_number: int) -> Simulation:
        balance_state_override = await self.get_balance_state_override(lp_execution.buy_token_address, int(lp_execution.buy_amount))
        lp_execution_transaction = self.create_lp_execution_transaction(lp_execution)
        lp_execution_transaction.state = balance_state_override
        return await self.simulate_transaction_via_tenderly(lp_execution_transaction, block_number=block_number)
    
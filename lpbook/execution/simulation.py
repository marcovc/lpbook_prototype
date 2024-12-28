import asyncio
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
from mergedeep import merge

logger = logging.getLogger(__name__)

load_dotenv()

QUASILABS_ADDRESS = os.getenv("QUASILABS_SUBMISSION_ADDRESS")

TENDERLY_ACCESS_KEY = os.getenv('TENDERLY_ACCESS_KEY')

UNISWAP_V3_CONTRACT_ADDRESS="0xe592427a0aece92de3edee1f18e0157c05861564"
WETH_ADDRESS="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"

WALLET_WITH_SOME_ETH = QUASILABS_ADDRESS

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

class NoAllowanceKeyException(Exception):
    pass

class NoBalanceKeyException(Exception):
    pass

class Simulator:
    def __init__(self, web3_client, session: aiohttp.ClientSession, settlement_address: str, state_directory: Path, discount_intrinsic_gas=False):
        self.web3_client = web3_client
        self.http_client = session
        self.settlement_address = settlement_address
        self.state_directory = state_directory
        with open(Path(__file__).parent / 'artifacts' / 'uniswap_v3.abi', 'r') as f:
            uniswap_v3_contract_abi = f.read()
        self.uniswap_v3_contract = web3_client.eth.contract(
            address=web3_client.to_checksum_address(UNISWAP_V3_CONTRACT_ADDRESS),
            abi=uniswap_v3_contract_abi
        )
        with open(Path(__file__).parent / 'artifacts' / 'erc20.abi', 'r') as f:
            self.erc20_abi = f.read()
        self.init_contract_slots()
        self.discount_intrinsic_gas = discount_intrinsic_gas

    def get_map_address_key_slot(self, map_slot, key1, key2=None):
        enc1 = self.web3_client.codec.encode(("address","uint256"),(key1, map_slot))
        kenc1 = web3.Web3.keccak(enc1)
        if key2 is None:
            return kenc1.hex()
        enc2 = self.web3_client.codec.encode(("address","bytes32"),(key2, kenc1))
        kenc2 = web3.Web3.keccak(enc2)
        return kenc2.hex()

    def get_balance_slot(self, token_address) -> Optional[int]:
        if token_address in self.balance_slots:
            return self.balance_slots[token_address]
        elif token_address == WETH_ADDRESS:
            return 3
        return None
    
    def get_balance_key(self, token_address) -> Optional[str]:
        slot = self.get_balance_slot(token_address)
        if slot is None:
            return None
        return self.get_map_address_key_slot(slot, self.settlement_address)

    def get_allowance_slot(self, token_address) -> Optional[int]:
        if token_address in self.allowance_slots:
            return self.allowance_slots[token_address]
        elif token_address == WETH_ADDRESS:
            return 4
        return None

    def get_allowance_key(self, token_address, spender) -> Optional[str]:
        slot = self.get_allowance_slot(token_address)
        if slot is None:
            return None
        return self.get_map_address_key_slot(slot, self.settlement_address, spender)

    def create_lp_execution_transaction(self, lp_execution: LPExecution) -> Transaction:
        return Transaction(from_=self.settlement_address, to=lp_execution.target, calldata=lp_execution.calldata)

    def tenderly_payload_from_transaction(self, transaction: Transaction, max_gas=4707788, block_number=None, generate_access_list=False) -> dict:
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
            'generate_access_list': generate_access_list,
            'save': True
        }
        if transaction.state is not None:
            json_data["state_objects"] =  {k: {"storage": v} for k, v in transaction.state.items()}

        if block_number is not None:
            json_data["block_number"] = block_number

        return json_data

    async def simulate_transaction_via_tenderly(self, transaction: Transaction, max_gas=4707788, block_number=None, generate_access_list=False) -> Simulation:
        json_data = self.tenderly_payload_from_transaction(transaction, max_gas=max_gas, block_number=block_number, generate_access_list=generate_access_list)
        async with self.http_client.post(
            'https://api.tenderly.co/api/v1/account/marcovc/project/project/simulate',
            headers=tenderly_headers,
            json=json_data
        ) as r:
            r = await r.json()
            #with open("last_tenderly_simulation.json", "w+") as f:  # TMP
            #    json.dump(r, f, indent=4)
            intrinsic_gas = 0
            if self.discount_intrinsic_gas and r["simulation"]["status"]:
                intrinsic_gas = r["transaction"]["transaction_info"]["intrinsic_gas"]
            return Simulation(
                success=r["simulation"]["status"], 
                gas_used=r["simulation"]["gas_used"] - intrinsic_gas, 
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


    def guess_slot(self, key, address1, address2=None):
        for slot in range(1000):
            if self.get_map_address_key_slot(slot, address1, address2) == key:
                return slot
        return None

    async def get_one_log(self, event):
        latest_block = await self.web3_client.eth.block_number;
        max_blocks_to_lookback = 1000
        page_size = 10
        cur_block = latest_block
        while cur_block >= latest_block - max_blocks_to_lookback:
            logs = await event.get_logs(fromBlock=cur_block-page_size, toBlock=cur_block)
            if len(logs)>0:
                return logs[0]
            cur_block -= page_size
        return None

    async def compute_balance_slot(self, token_address):
        token_contract = self.web3_client.eth.contract(
            address=self.web3_client.to_checksum_address(token_address),
            abi=self.erc20_abi
        )
        # Any two addresses would do, but from_ needs to have enough eth for the simulation
        from_ = WALLET_WITH_SOME_ETH
        to = token_address
        calldata = token_contract.encodeABI(fn_name="balanceOf", args=[
            self.web3_client.to_checksum_address(self.settlement_address)
        ])
        simulation = await self.web3_client.eth.create_access_list({
            'from': self.web3_client.to_checksum_address(from_), 
            'to': self.web3_client.to_checksum_address(to), 
            'data': calldata,
            'gas': 50000,
        })
        for access in simulation.accessList:
            if access.address.lower() != token_address:
                continue
            for key in access.storageKeys:
                slot = self.guess_slot(key.hex(), address1=self.settlement_address)
                if slot is not None:
                    self.balance_slots[token_address] = slot 
                    self.save_contract_slots()
                    return slot
        logger.warn(f"Could not compute balance slot for token {token_address}: {simulation}")
        return None
    
    async def compute_allowance_slot(self, token_address):
        token_contract = self.web3_client.eth.contract(
            address=self.web3_client.to_checksum_address(token_address),
            abi=self.erc20_abi
        )
        # Any two addresses would do, but from_ needs to have enough eth for the simulation
        from_ = WALLET_WITH_SOME_ETH
        to = token_address
        dummy_spender = "0xe592427a0aece92de3edee1f18e0157c05861564"
        calldata = token_contract.encodeABI(fn_name="allowance", args=[
            self.web3_client.to_checksum_address(self.settlement_address), 
            self.web3_client.to_checksum_address(dummy_spender)
        ])
        simulation = await self.web3_client.eth.create_access_list({
            'from': self.web3_client.to_checksum_address(from_), 
            'to': self.web3_client.to_checksum_address(to), 
            'data': calldata,
            'gas': 50000,
        })
        for access in simulation.accessList:
            if access.address.lower() != token_address:
                continue
            for key in access.storageKeys:
                slot = self.guess_slot(key.hex(), address1=self.settlement_address, address2=dummy_spender)
                if slot is not None:
                    self.allowance_slots[token_address] = slot 
                    self.save_contract_slots()
                    return slot
        return None
        
    # Try to guess balance key of a ERC20 contract.
    async def compute_balance_key(self, token_address: str) -> str:
        balance_key = self.get_balance_key(token_address)
        if balance_key is not None:
            return balance_key
        logger.debug(f"Cache miss for balance slot for token {token_address}.")
        balance_slot = await self.compute_balance_slot(token_address)
        if balance_slot is not None:
            return self.get_balance_key(token_address)
        raise NoBalanceKeyException("Failed to compute balance key.")

    # Try to guess allowance key of a ERC20 contract.
    async def compute_allowance_key(self, token_address: str, spender: str) -> str:
        allowance_key = self.get_allowance_key(token_address, spender)
        if allowance_key is not None:
            return allowance_key
        logger.debug(f"Cache miss for allowance slot for token {token_address}.")
        allowance_slot = await self.compute_allowance_slot(token_address)
        if allowance_slot is not None:
            return self.get_allowance_key(token_address, spender)
        raise NoAllowanceKeyException("Failed to compute allowance key.")

    def init_contract_slots(self):
        self.balance_slots = {}
        self.allowance_slots = {}
        try:
            with open(self.state_directory / "contract_slots.pickle", "rb") as f:
                self.balance_slots, self.allowance_slots = pickle.load(f)
        except FileNotFoundError:
            logger.error("Could not load contract slots. Starting from scratch.")
            pass

    def save_contract_slots(self):
        with open(self.state_directory / "contract_slots.pickle", "wb+") as f:
            pickle.dump((self.balance_slots, self.allowance_slots), f)

    async def get_balance_state_override(self, token_address: str, balance: int) -> dict:
        key = await self.compute_balance_key(token_address)
        return {token_address: {key: to_hex256_string(balance)}}

    async def get_allowance_state_override(self, token_address: str, spender: str, balance: int) -> dict:
        key = await self.compute_allowance_key(token_address, spender)
        return {token_address: {key: to_hex256_string(balance)}}

    async def simulate_execution(self, lp_execution: LPExecution, block_number: int) -> Simulation:
        balance_state_override = await self.get_balance_state_override(lp_execution.buy_token_address, int(lp_execution.buy_amount))
        allowance_state_override = await self.get_allowance_state_override(lp_execution.buy_token_address, lp_execution.approved_spender, int(lp_execution.buy_amount))
        state_override = {}
        merge(state_override, balance_state_override, allowance_state_override)
        lp_execution_transaction = self.create_lp_execution_transaction(lp_execution)
        lp_execution_transaction.state = state_override
        return await self.simulate_transaction_via_tenderly(lp_execution_transaction, block_number=block_number)
    
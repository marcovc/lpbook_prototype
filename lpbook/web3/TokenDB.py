from typing import Optional

from lpbook.util import Token
from . import create_token_from_web3
import asyncio
import jsonpickle

from web3.exceptions import ContractLogicError, BadFunctionCallOutput

class TokenDB:
    def __init__(self, web3_client, state_directory):
        self.web3_client = web3_client
        self.state_directory = state_directory
        self.tokens_by_address = {}
        self.bad_tokens = set()
        self.load_state()

    async def async_del(self):
        self.dump_state()

    def load_state(self):
        try:
            with open(self.state_directory / "token_db.json", "r") as f:
                self.tokens_by_address, self.bad_tokens = jsonpickle.decode(f.read())
        except FileNotFoundError:
            pass

    def dump_state(self):
        with open(self.state_directory / "token_db.json", "w+") as f:
            f.write(jsonpickle.encode((self.tokens_by_address, self.bad_tokens)))

    # Returns None for weird tokens (can't decode token from its smartcontract).
    async def get(self, token_address) -> Optional[Token]:
        if token_address in self.tokens_by_address:
            return self.tokens_by_address[token_address]
        if token_address in self.bad_tokens:
            return None
        try:
            token = await asyncio.to_thread(create_token_from_web3, token_address, self.web3_client)
        except (ContractLogicError, OverflowError, BadFunctionCallOutput):
            self.bad_tokens.add(token_address)
            return None            
        self.tokens_by_address[token_address] = token
        return token
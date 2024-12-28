import asyncio
import json
import logging
import logging.config
import os
#from diskcache import Index
import time
from threading import Thread

import aiohttp
from dotenv import load_dotenv
from web3 import Web3

from lpbook.lps.uniswap_v3 import (SyncedUniV3, UniV3Driver,
                                 UniV3EventLog, UniV3RandomStateProxy)

from .web3.event_stream import EventNotifier
from .web3.block_stream import BlockStream
from .LPCache import LPCache

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=True)

logger = logging.getLogger(__name__)

load_dotenv() 

ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')
INFURA_ID = os.getenv('INFURA_ID')

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_ID}'))
#w3 = Web3(Web3.HTTPProvider(f'wss://mainnet.infura.io/ws/v3/{INFURA_ID}'))

#w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/270Ng0vUmrsinDLbgeNAldwNmuO8aDC4'))

addresses={
    'USDCWETH': Web3.to_checksum_address('0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8'),
    'DAIUSDC': Web3.to_checksum_address('0x5777d92f208679db4b9778590fa3cab3ac9e2168')
}

def get_abi(address):
    import requests
    ABI_ENDPOINT = 'https://api.etherscan.io/api?module=contract&action=getabi&address='
    response = requests.get('%s%s'%(ABI_ENDPOINT, address), params={"apikey": ETHERSCAN_API_KEY})
    response_json = response.json()
    return response_json['result']

print(w3.isConnected())

"""
contract_abi = get_abi(addresses["USDCWETH"])
UniV3 = w3.eth.contract(abi=contract_abi)

def event_callback(decoded_event):
    print(decoded_event)

event_notifier = EventNotifier(UniV3, event_callback, [UniV3.events.Swap, UniV3.events.Burn, UniV3.events.Mint], list(addresses.values()), w3, 10)
asyncio.run(event_notifier.run())
"""

from lpbook.lps.uniswap_v3.subgraph import UniV3GraphQLClient


async def main():

    block_stream = BlockStream(f'wss://mainnet.infura.io/ws/v3/{INFURA_ID}')

    async with aiohttp.ClientSession() as session:

        """
        uniswap_v3_gql_client = UniV3GraphQLClient(session)

        #async for p in client.get_lps({"block":14088107,"token0_in":["0x6b175474e89094c44da98b954eedeac495271d0f"]}):
        #    print(p)
        #await client.get_lp_state_and_ticks("0x5777d92f208679db4b9778590fa3cab3ac9e2168")

        #lps_and_ticks = await uniswap_v3_gql_client.get_lps_state_and_ticks(
        #    {"id_in": ["0x5777d92f208679db4b9778590fa3cab3ac9e2168", "0xcbcdf9626bc03e24f779434178a73a0b4bad62ed"]},
        #    {}
        #)
        #print(lps_and_ticks)

        lp_ids = ["0x5777d92f208679db4b9778590fa3cab3ac9e2168", "0xcbcdf9626bc03e24f779434178a73a0b4bad62ed"]
        uniswap_v3_thegraph_feed = UniV3RandomStateProxy(lp_ids, uniswap_v3_gql_client)
        uniswap_v3_blockchain_feed = UniV3EventLog(lp_ids, w3, block_stream)
        synced_uniswap_v3 = SyncedUniV3(uniswap_v3_thegraph_feed, uniswap_v3_blockchain_feed)

        async def call_api():
            while True:
                print("calling api:", synced_uniswap_v3()) 
                await asyncio.sleep(5)

        await asyncio.gather(
            synced_uniswap_v3.run(),
            call_api()
        )  
        """
        uniswap_v3_driver = UniV3Driver(block_stream, session, w3)
        lp_cache = LPCache([uniswap_v3_driver])

        async def call_api():
            lp_ids = {"0x6b175474e89094c44da98b954eedeac495271d0f", "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"}
            while True:
                print("calling api:", lp_cache.get_lps_involving_tokens(lp_ids)) 
                await asyncio.sleep(60)

        await asyncio.gather(
            block_stream.run(),
            lp_cache.run(),            
            call_api()
        )  

asyncio.run(main())



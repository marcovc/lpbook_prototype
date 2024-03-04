import requests
import argparse
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')


def get_abi(address):
    ABI_ENDPOINT = 'https://api.etherscan.io/api?module=contract&action=getabi&' \
        f'address={address}&apikey={ETHERSCAN_API_KEY}'
    response = requests.get(ABI_ENDPOINT)
    response_json = response.json()
    return response_json['result']


def get_abis(addresses):
    return [get_abi(address) for address in addresses]


if __name__ == '__main__':
    # Process command line arguments.
    parser = argparse.ArgumentParser(
        description='Retrieve contract ABIs from etherscan.')

    parser.add_argument(
        'output_dir',
        type=Path,
        help='Directory to store contract ABIs.',
    )

    parser.add_argument(
        'addresses',
        type=str,
        help='Contract addresses.',
        nargs='*'
    )

    args = parser.parse_args()

    abis = get_abis(args.addresses)
    for address, abi in zip(args.addresses, abis):
        with open(args.output_dir / f'{address}.abi', 'w+') as f:
            f.write(abi)

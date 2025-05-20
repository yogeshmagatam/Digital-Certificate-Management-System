from web3 import Web3
from config import Config

w3 = Web3(Web3.HTTPProvider(Config.BLOCKCHAIN_PROVIDER))
contract = w3.eth.contract(address=Config.CONTRACT_ADDRESS, abi=[{
    "inputs": [{"internalType": "string", "name": "hash", "type": "string"}],
    "name": "storeCertificateHash",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
}])

def anchor(hash_str, account, private_key):
    tx = contract.functions.storeCertificateHash(hash_str).build_transaction({
        'from': account,
        'nonce': w3.eth.get_transaction_count(account),
        'gas': 2000000,
        'gasPrice': w3.to_wei('50', 'gwei')
    })
    signed = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return w3.to_hex(tx_hash)

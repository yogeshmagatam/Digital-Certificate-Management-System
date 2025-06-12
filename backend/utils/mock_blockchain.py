import time
import hashlib

dummy_chain = []

def anchor(data):
    """Simulates storing data on a blockchain by hashing it and storing in a list"""
    timestamp = int(time.time())
    tx_hash = hashlib.sha256(f"{data}-{timestamp}".encode()).hexdigest()
    
    block = {
        "index": len(dummy_chain) + 1,
        "timestamp": timestamp,
        "data": data,
        "tx_hash": tx_hash
    }
    dummy_chain.append(block)
    return tx_hash

def get_all_blocks():
    """Returns the mock chain"""
    return dummy_chain

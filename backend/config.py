import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', "mongodb://localhost:27017")
    JWT_SECRET = os.getenv('JWT_SECRET')
    IPFS_API_URL = os.getenv('IPFS_API_URL')
    BLOCKCHAIN_PROVIDER = os.getenv('BLOCKCHAIN_PROVIDER')
    CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
    ETH_ACCOUNT = os.getenv('ETH_ACCOUNT')
    ETH_KEY = os.getenv('ETH_KEY')
    IPFS_PROJECT_ID = os.getenv("IPFS_PROJECT_ID")
    IPFS_PROJECT_SECRET = os.getenv("IPFS_PROJECT_SECRET")

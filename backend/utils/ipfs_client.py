import requests
from requests.auth import HTTPBasicAuth
import os
from config import Config

IPFS_PROJECT_ID = os.getenv("IPFS_PROJECT_ID")
IPFS_PROJECT_SECRET = os.getenv("IPFS_PROJECT_SECRET")

def upload_file(file_path):
    url = "https://ipfs.infura.io:5001/api/v0/add"
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(
            url,
            files=files,
            auth=HTTPBasicAuth(IPFS_PROJECT_ID, IPFS_PROJECT_SECRET)
        )
    if response.status_code == 200:
        return response.json()["Hash"]
    else:
        raise Exception(f"IPFS upload failed: {response.text}")

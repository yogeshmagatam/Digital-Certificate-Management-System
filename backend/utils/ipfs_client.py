# utils/ipfs_client.py

import requests
from config import Config

def upload_file(file_path):
    url = f"{Config.IPFS_API_URL}/api/v0/add"

    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files, auth=(Config.IPFS_PROJECT_ID, Config.IPFS_PROJECT_SECRET))

    if response.status_code == 200:
        return response.json()  # will contain 'Hash', 'Name', etc.
    else:
        raise Exception(f"IPFS upload failed: {response.text}")

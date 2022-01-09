import json
import os
import requests
import pandas as pd

def extract_from_api():
    headers = requests.utils.default_headers()
    response = requests.get(
        'https://data.sfgov.org/resource/wr8u-xric.json',
        headers=headers,
        verify=False
    )

    if response.status_code == 200:
        incidents = json.loads(response.text)
        print("extraction done")

from concurrent.futures import ThreadPoolExecutor
import requests
from timer import Timer
import json


URL = 'https://httpbin.org/uuid'

def fetch(URL):
    response = requests.get(URL)
    data = json.loads(response.text)
    print(data['uuid'])

if __name__ == '__main__':
    with Timer():
        with ThreadPoolExecutor(max_workers=40) as thread:
            thread.map(fetch, [URL] * 50)
            thread.shutdown(wait=True)

# takes ~4 seconds

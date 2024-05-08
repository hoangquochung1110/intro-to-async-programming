from multiprocessing import Pool
import requests
import json
from timer import Timer


URL = 'https://httpbin.org/uuid'

def fetch():
    response = requests.get(URL)
    data = json.loads(response.text)
    print(data['uuid'])

if __name__ == '__main__':
    with Timer():
        with Pool() as pool:
            results = pool.starmap(fetch, [() for _ in range(50)])

# take ~6 seconds

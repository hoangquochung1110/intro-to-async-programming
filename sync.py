import json
import requests
from timer import Timer

URL = 'https://httpbin.org/uuid'

def fetch(url):
    response = requests.get(url)
    data = json.loads(response.text)
    print(data['uuid'])


def main():
    with Timer():
        for _ in range(50):
            fetch(URL)

main()
# take ~50 seconds

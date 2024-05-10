from celery import Celery
from timer import Timer
import json
import requests

URL = 'https://httpbin.org/uuid'

BROKER_URL = 'redis://localhost:6379/0'
RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery(__name__, broker=BROKER_URL, backend=RESULT_BACKEND)


@app.task(name='fetch')
def fetch():
    res = requests.get(URL)
    return res.json()['uuid']


def main():
    with Timer():
        for i in range(50):
            res = fetch.delay()
            print(res)


if __name__ == '__main__':
    main()

# takes ~0.1 seconds

import aiohttp
import asyncio
from timer import Timer


URL = 'https://httpbin.org/uuid'

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json()
            print(data['uuid'])


async def main():
    async with aiohttp.ClientSession() as session:
        with Timer():
            batch = [
                fetch() for _ in range(50)
            ]
            results = await asyncio.gather(*batch)

asyncio.run(main())
# take ~ 2 seconds

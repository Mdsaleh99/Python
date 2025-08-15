import asyncio
import aiohttp

# https://docs.aiohttp.org/en/stable/

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3 
    print(urls)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        # e.g:  tasks = [t1, t2, t3]
        await asyncio.gather(*tasks) # *tasks (*) because we want to unpack the list of tasks
        # e.g:  await asyncio.gather(t1, t2, t3) # instead of *tasks it is like this unpacking the individual tasks


asyncio.run(main())
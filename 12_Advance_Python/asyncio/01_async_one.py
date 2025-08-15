import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2) # this async and await does not block main thread
    print("chai is ready")

asyncio.run(brew_chai())
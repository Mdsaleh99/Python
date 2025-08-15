import asyncio
import time

async def brew_chai(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2) # await means wait but in a non-blocking way
    # time.sleep(2)  # it is a blocking
    print(f"{name} is ready...")


async def main():
    await asyncio.gather(
        brew_chai("Masala chai"),
        brew_chai("Ginger chai"),
        brew_chai("Lemon Tea")
    )

asyncio.run(main())
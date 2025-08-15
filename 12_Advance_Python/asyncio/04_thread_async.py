import asyncio
import time
from concurrent.futures import ThreadPoolExecutor  # Creates a pool of threads for running blocking (CPU / I/O) functions


def check_stocks(item):
    """Simulate a slow, blocking function (e.g. network / disk / API call).
    We purposefully use time.sleep (blocking) instead of asyncio.sleep (non‑blocking)
    to show why we need a thread executor.
    """
    print(f"Checking {item} in store...")
    time.sleep(2)  # BLOCKS the current thread (would freeze the event loop if run directly)
    return f"{item} Stock: 45"


async def main():
    # get_running_loop(): returns the currently running event loop instance.
    # We need the loop to ask it to offload work to another thread.
    loop = asyncio.get_running_loop()

    # ThreadPoolExecutor: manages a pool of worker threads. Each blocking function call
    # can run in one of these threads so the async event loop stays responsive.
    # Using it as a context manager automatically shuts it down when done.
    with ThreadPoolExecutor() as pool:
        # * run_in_executor lets in asyncio to run a async function but in another thread
        # loop.run_in_executor(executor, func, *args): run the blocking 'func' in a separate
        # thread (or process pool). It returns an awaitable that resolves with the function's return value.
        # If you pass 'None' as the executor, it uses the default loop-wide thread pool.
        result = await loop.run_in_executor(pool, check_stocks, "Masala Chai")
        print(result)


# asyncio.run: starts an event loop, runs the coroutine, then closes the loop.
asyncio.run(main())
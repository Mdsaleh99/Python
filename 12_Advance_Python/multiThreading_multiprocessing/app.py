# concurrency is the ability to run multiple tasks simultaneously - threading.Thread, asyncio
# parallelism is the ability to run multiple tasks at the same time - multiprocessing.Process, concurrent.futures.ProcessPoolExecutor

# Concurrency → You work on multiple dishes at the same time, but not literally at the exact same moment.
# You switch between them:
    # Chop onions → start boiling water → stir the soup → return to onions.
    # This is like multitasking — you're not doing both chopping and stirring at exactly the same time, but you’re managing both.


# Parallelism → You have multiple cooks in the kitchen, each working on their own dish at the same time.
# One cooks pasta, another grills chicken, both happening simultaneously.
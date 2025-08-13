# GIL - Global Interpreter Lock
# The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once.
# This means that even in a multi-threaded program, only one thread can execute Python code at a time.
# The GIL can be a bottleneck in CPU-bound and multithreaded code.
# Race conditions can occur when multiple threads access shared data and try to change it at the same time.

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")


thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")
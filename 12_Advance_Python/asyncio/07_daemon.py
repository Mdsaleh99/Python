import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done")

# Non-daemon thread (default) → Main program waits for it to finish before exiting.
# Daemon thread → Runs in the background, and the main program doesn’t wait for it; it stops immediately when the main program ends.

# Profiling → Measuring performance (time, memory, CPU usage) to find bottlenecks.
# Tools: cProfile, memory_profiler, py-spy, https://github.com/benfred/py-spy, https://github.com/nvdv/vprof
# Command: python -m cProfile -s time myscript.py
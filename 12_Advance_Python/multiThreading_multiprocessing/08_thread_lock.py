import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        counter += 1
        # with lock:
        #     counter += 1


threads = [threading.Thread(target=increment) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")
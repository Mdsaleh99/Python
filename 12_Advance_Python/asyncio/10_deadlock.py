import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task_1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquired lock b")

def task_2():
    with lock_b:
        print("Task 2 acquired lock b")
        with lock_a:
            print("Task 2 acquired lock a")


# threading.Thread(target=task_1).start()
# threading.Thread(target=task_2).start()

t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)

t1.start()
t2.start()


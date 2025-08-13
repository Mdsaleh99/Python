from multiprocessing import Process
import time

# A program can work with multiple processes and each process can be divided into threads

# Process doesn't know the which is the entry point to start, so we need to do if __name__ == "__main__": inside the we have to write all the code

"""
def crunch_number():
    print(f"Started the count process")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Finished the count process")


start = time.time()

p1 = Process(target=crunch_number)
p2 = Process(target=crunch_number)

p1.start()
p2.start()

p1.join()
p2.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")
"""

if __name__ == "__main__":
    def crunch_number():
        print(f"Started the count process")
        count = 0
        for _ in range(100_000_000):
            count += 1
        print(f"Finished the count process")


    start = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken: {end - start:.2f} seconds")
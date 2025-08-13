import threading
import time

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk boiled.")

def brew_coffee():
    print("Brewing coffee...")
    time.sleep(3)
    print("Coffee brewed.")

start = time.time()
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=brew_coffee)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Coffee is ready in {end - start:.2f} seconds")
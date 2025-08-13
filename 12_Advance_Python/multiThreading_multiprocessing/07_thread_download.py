import threading
import requests
import time

# threading actually shine in i/o bound operations like disk read/write, web requests
# Each process gets it's own memory, threads can share the memory because they are all in one process itself

def download(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(response.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


end = time.time()

print(f"All downloads done in {end - start:.2f} seconds")
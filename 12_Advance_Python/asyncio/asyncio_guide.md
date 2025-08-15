# Python Async IO (asyncio) – From Basics to Advanced

This guide gives a layered path from simple concepts through advanced patterns of `asyncio` in modern Python (3.11+ mindset). Focus is on clarity, correctness, and practical usage.

---

## 1. Why Async IO?

| Situation                                           | Good Fit For Async?      | Why                                          |
| --------------------------------------------------- | ------------------------ | -------------------------------------------- |
| Many network calls (APIs, sockets, DB over network) | ✅                       | Overlap waiting time.                        |
| Heavy CPU math                                      | ❌ (use processes/NumPy) | CPU keeps loop busy; no benefit.             |
| File system heavy operations                        | ⚠️ Limited               | Most FS ops are blocking except via threads. |
| UI / Servers handling many connections              | ✅                       | Keeps responsiveness high.                   |
| Small number of long CPU tasks                      | ❌                       | No waiting to hide.                          |

Async IO = Cooperative multitasking around I/O waits. Not parallel CPU execution (unless offloaded).

---

## 2. Core Vocabulary

| Term        | Meaning                                                            |
| ----------- | ------------------------------------------------------------------ |
| Coroutine   | An `async def` function; returns a coroutine object until awaited. |
| Awaitable   | Object usable in `await` (coroutine, Task, Future).                |
| Event Loop  | Scheduler orchestrating ready tasks + I/O events + callbacks.      |
| Task        | Wrapper scheduling a coroutine for concurrent execution.           |
| Future      | Low-level placeholder for a result set later.                      |
| Cooperative | Coroutines yield at `await` points; no preemption.                 |

Mental model: `asyncio` runs one thread (usually) executing one piece of Python code at a time; concurrency is created by _switching at awaits_.

---

## 3. Minimal Example

```python
import asyncio

async def greet():
    await asyncio.sleep(1)
    return "hello"

async def main():
    task = asyncio.create_task(greet())  # schedule concurrently
    print("Waiting...")
    result = await task
    print(result)

asyncio.run(main())
```

Key points:

-   `asyncio.run()` creates & closes the event loop (preferred top-level starting in 3.7+).
-   `await` suspends the coroutine, returning control to the loop.

---

## 4. Coroutines vs Tasks

-   A coroutine object does nothing until awaited or turned into a Task.
-   `asyncio.create_task(coro)` starts it immediately (concurrently).
-   `await coro` runs it inline (no concurrency beyond internal awaits).

```python
# Sequential
await coro_a()
await coro_b()   # starts only after a finishes

# Concurrent
task_a = asyncio.create_task(coro_a())
task_b = asyncio.create_task(coro_b())
await task_a; await task_b
```

---

## 5. Running Many Coroutines

### 5.1 `asyncio.gather`

```python
results = await asyncio.gather(*(fetch(url) for url in urls))
```

-   Fails fast: if one raises, others continue but the first exception bubbles; remaining exceptions suppressed (you can inspect with `return_exceptions=True`).

### 5.2 TaskGroup (Python 3.11+)

Structured concurrency.

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        for u in urls:
            tg.create_task(fetch(u))
# Exiting the block waits for all tasks; exceptions become ExceptionGroup.
```

Advantages: automatic cancellation of siblings on error.

---

## 6. Timeouts & Cancellation

### 6.1 Timeout

```python
try:
    await asyncio.wait_for(do_io(), timeout=2.0)
except asyncio.TimeoutError:
    ...
```

### 6.2 Cancellation Flow

```python
task = asyncio.create_task(do_io())
# later
task.cancel()
try:
    await task
except asyncio.CancelledError:
    print("Cancelled cleanly")
```

Cancellation raises `CancelledError` at the next await inside the coroutine.

### 6.3 Shielding

```python
await asyncio.shield(critical_task)
```

Prevents external cancellation from propagating (unless the task itself gets cancelled internally).

---

## 7. Async Context Managers & Iterators

### 7.1 Async Context Manager

```python
class AsyncResource:
    async def __aenter__(self):
        await asyncio.sleep(0)
        return self
    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0)

async with AsyncResource() as r:
    ...
```

### 7.2 Async Iterator / Generator

```python
class AsyncCounter:
    def __init__(self, n): self.n=n
    def __aiter__(self): return self
    async def __anext__(self):
        if self.n <= 0: raise StopAsyncIteration
        await asyncio.sleep(0)
        self.n -= 1
        return self.n

async for x in AsyncCounter(3):
    print(x)
```

Async generators:

```python
async def gen():
    for i in range(3):
        await asyncio.sleep(0)
        yield i
```

---

## 8. Avoiding Blocking Code

Blocking = starves event loop. Common pitfalls:

-   Calling time.sleep() instead of asyncio.sleep()
-   Heavy CPU loops in async function
-   Blocking libraries (e.g., requests). Use `aiohttp` or a thread executor.

### 8.1 Wrapping Blocking Call

```python
await asyncio.to_thread(blocking_func, *args)
```

(Preferred over manual `loop.run_in_executor()` in 3.9+.)

### 8.2 CPU-bound Offload

```python
loop = asyncio.get_running_loop()
result = await loop.run_in_executor(None, cpu_heavy)  # process pool if needed
```

For true parallel CPU: use `ProcessPoolExecutor` (cost higher; batch work).

---

## 9. Backpressure & Rate Limiting

### 9.1 Semaphore for Concurrency Limit

```python
sem = asyncio.Semaphore(10)
async def limited_fetch(url):
    async with sem:
        return await fetch(url)
```

### 9.2 Producer/Consumer with Queue

```python
queue = asyncio.Queue()

async def producer():
    for item in range(50):
        await queue.put(item)
    await queue.put(None)   # sentinel

async def consumer():
    while True:
        item = await queue.get()
        if item is None:
            await queue.put(None)  # pass sentinel
            break
        try:
            await process(item)
        finally:
            queue.task_done()

await asyncio.gather(producer(), consumer())
```

### 9.3 Handling Burst Inputs

Strategy: queue with maxsize; producers `await queue.put()` will naturally slow. Consider dropping or batching if queue saturates.

---

## 10. Error Handling Patterns

### 10.1 Gather with Exceptions

```python
results = await asyncio.gather(*tasks, return_exceptions=True)
for r in results:
    if isinstance(r, Exception):
        ...
```

### 10.2 TaskGroup ExceptionGroup

```python
async with asyncio.TaskGroup() as tg:
    tg.create_task(task_a())
    tg.create_task(task_b())
# If both raise, an ExceptionGroup surfaces.
```

### 10.3 Global Task Error Logging

Un-awaited tasks whose exceptions are never observed produce warnings. Always keep references or wrap creation with logging callback.

```python
async def supervisor():
    t = asyncio.create_task(worker())
    t.add_done_callback(lambda fut: print(fut.exception()))
```

---

## 11. Cancellation Gotchas

-   Try/finally will still execute during cancellation — good for cleanup.
-   Swallowing `CancelledError` without re-raising can leave higher-level tasks hanging (structured concurrency helps).
-   Use short awaits (e.g., `await asyncio.sleep(0)`) in long loops to stay responsive to cancellation.

Cancellation-friendly loop:

```python
async def loop_work():
    try:
        while True:
            await do_step()
            await asyncio.sleep(0)  # yield
    except asyncio.CancelledError:
        await cleanup()
        raise
```

---

## 12. Ordering & Fairness

The loop schedules ready tasks in FIFO of sort; tasks that await often yield fairness. Long CPU steps hinder fairness—break them.

Chunking pattern:

```python
for chunk in chunk_iter(big_items, 500):
    process_chunk(chunk)   # small synchronous work
    await asyncio.sleep(0) # let others run
```

---

## 13. Performance Tuning

| Issue                        | Symptom              | Mitigation                                      |
| ---------------------------- | -------------------- | ----------------------------------------------- |
| Too many tasks               | Memory/time overhead | Batch, limit concurrency with Semaphore         |
| Blocking call                | Latency spikes       | Wrap in `to_thread` / use async lib             |
| Tiny tasks overhead          | High scheduling cost | Aggregate / pipeline fewer awaits               |
| Unnecessary context switches | Lower throughput     | Avoid gratuitous `await sleep(0)` if not needed |

### 13.1 Use uvloop (Optional, \*nix Only)

3rd-party event loop (drop-in) often faster for network heavy workloads.

```python
import asyncio, uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
```

### 13.2 Profiling

-   Wall time: `asyncio.run(main())` with `py-spy` or `yappi`.
-   Await tree: `aiomonitor`, `asyncio.run(debug=True)` for debug mode.

### 13.3 Debug Mode

```python
asyncio.run(main(), debug=True)
```

Adds slow-safety checks (e.g., detects slow callbacks, un-awaited tasks).

---

## 14. Streams & Low-Level APIS

### 14.1 High-Level Streams

```python
reader, writer = await asyncio.open_connection('example.com', 80)
writer.write(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
await writer.drain()
line = await reader.readline()
writer.close()
await writer.wait_closed()
```

### 14.2 Subprocesses

```python
proc = await asyncio.create_subprocess_exec('python', '--version', stdout=asyncio.subprocess.PIPE)
stdout, _ = await proc.communicate()
print(stdout.decode())
```

### 14.3 Protocol / Transport (Lower-level)

Use when you need fine-grained control, performance, or custom framing. Usually streams suffice; prefer them unless optimizing.

---

## 15. Context Variables

`contextvars` provide context local to a task (unlike thread-locals across tasks). Useful for tracing, request IDs.

```python
import contextvars
request_id = contextvars.ContextVar('request_id')

async def handle(i):
    request_id.set(i)
    await asyncio.sleep(0)
    log(request_id.get())
```

---

## 16. Structured Concurrency (TaskGroup Benefits)

| Problem Without       | Solution With TaskGroup         |
| --------------------- | ------------------------------- |
| Orphan tasks on error | All children cancelled together |
| Missed exceptions     | Bundled ExceptionGroup surfaced |
| Complex manual joins  | Scope-based automatic wait      |

Prefer TaskGroup for launching sibling tasks that form a unit of work.

---

## 17. Testing Async Code

### 17.1 pytest-asyncio

```python
import pytest

@pytest.mark.asyncio
async def test_fetch():
    data = await fetch_one()
    assert data['ok']
```

(Or with new mode: configure `asyncio_mode=auto` in pytest.ini.)

### 17.2 Timeouts in Tests

Use `asyncio.wait_for` or plugin (e.g., `pytest-timeout`).

### 17.3 Faking I/O

Inject stub async functions returning known values; or use libraries like `aresponses` for HTTP mocking.

---

## 18. Migration Strategy (Sync → Async)

1. Identify I/O boundaries (network calls).
2. Replace blocking libs with async equivalents (requests → aiohttp, psycopg2 → asyncpg).
3. Wrap temporarily with `to_thread` when replacement not ready.
4. Introduce async at top-level API; propagate outward.
5. Gradually remove `run_in_executor` wrappers as native async versions adopted.

Avoid mixing two event loops; keep one `asyncio.run` entry point.

---

## 19. Integration With Threads / Processes

| Need                     | Approach                                            |
| ------------------------ | --------------------------------------------------- |
| Use legacy blocking lib  | `await asyncio.to_thread(blocking)`                 |
| CPU heavy                | `loop.run_in_executor(ProcessPoolExecutor(), func)` |
| Background periodic task | Create task + cancellation handling                 |

Example periodic task:

```python
async def ticker(interval, stop_event):
    try:
        while not stop_event.is_set():
            print("tick")
            await asyncio.sleep(interval)
    except asyncio.CancelledError:
        print("stopping ticker")
        raise
```

---

## 20. Patterns Catalog

| Pattern                         | Description                  | Snippet Idea                         |
| ------------------------------- | ---------------------------- | ------------------------------------ |
| Fan-out gather                  | Launch many tasks, await all | `await gather(*tasks)`               |
| Pipeline                        | Queues connecting stages     | `asyncio.Queue()` stages             |
| Supervisor                      | Monitor & restart            | Loop over tasks, recreate on failure |
| Timeout + fallback              | Try fast source else slower  | `wait_for` + except                  |
| Rate limit                      | Semaphore / token bucket     | Acquire before fetch                 |
| Retry with backoff              | Robust I/O                   | Async sleep with jitter              |
| Scatter/Gather with cancel slow | Use `wait` FIRST_COMPLETED   | Cancel rest                          |

Scatter/Gather earliest:

```python
done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
for p in pending: p.cancel()
first = done.pop().result()
```

---

## 21. Memory & Resource Leaks

| Leak Source                  | Symptom             | Fix                            |
| ---------------------------- | ------------------- | ------------------------------ |
| Unclosed network sessions    | Open sockets        | `async with ClientSession()`   |
| Forgotten `writer.close()`   | Hanging connections | Always close/await wait_closed |
| Detached tasks never awaited | Warning at exit     | Track tasks; TaskGroup         |
| Accumulating Queue backlog   | Memory spike        | Apply backpressure (maxsize)   |

Use `tracemalloc` + instrumentation for long-running services.

---

## 22. Logging & Tracing

Add context (task name, request id).

```python
asyncio.current_task().get_name()
```

Set names:

```python
t = asyncio.create_task(coro(), name="fetch-user-42")
```

Tracing: OpenTelemetry has async integrations; ensure contextvars propagate.

---

## 23. Security Considerations

-   Validate inputs early (async does not sanitize automatically).
-   Beware SSRF / open redirect when performing many network calls concurrently.
-   Rate-limit outbound calls to avoid overwhelming upstream systems.
-   Cancellation cleanup must release secrets / wipe buffers.

---

## 24. Choosing Among Async Libraries

| Goal                                      | Library                             |
| ----------------------------------------- | ----------------------------------- |
| HTTP client                               | `aiohttp`, `httpx`                  |
| Web server                                | `FastAPI` / `Starlette` / `aiohttp` |
| Database (Postgres)                       | `asyncpg`                           |
| Redis                                     | `aioredis`                          |
| Messaging                                 | `aio-pika`, `aiokafka`              |
| Alternative loop & structured concurrency | `trio`                              |

`trio` promotes structured concurrency by default; consider if starting greenfield.

---

## 25. Quick Anti-Patterns & Fixes

| Anti-Pattern                            | Problem                                    | Fix                                       |
| --------------------------------------- | ------------------------------------------ | ----------------------------------------- |
| `await` inside CPU loop each iteration  | Slow context switching                     | Batch work, single await per chunk        |
| Creating thousands of tasks instantly   | Memory blow-up                             | Semaphore / pool                          |
| Forgetting `await` before coroutine     | Gets `coroutine was never awaited` warning | Always await or schedule                  |
| Catch-all `except Exception:` + swallow | Masks bugs                                 | Log/re-raise; structured handling         |
| Busy wait loop                          | Wastes CPU                                 | Use `await asyncio.sleep()` appropriately |

---

## 26. Comprehensive Example (Pipeline + Rate Limit + Cancellation)

```python
import asyncio, random, time

async def fetch(n):
    await asyncio.sleep(random.uniform(0.05, 0.2))
    if random.random() < 0.05: raise RuntimeError(f"boom {n}")
    return n * 2

async def transform(x):
    await asyncio.sleep(0)  # pretend small async op
    return x + 1

async def producer(out_q, total):
    for i in range(total):
        await out_q.put(i)
    await out_q.put(None)  # sentinel

async def worker(in_q, out_q, sem):
    while True:
        item = await in_q.get()
        if item is None:
            await in_q.put(None)
            break
        async with sem:  # rate limit
            try:
                data = await fetch(item)
            except Exception as e:
                data = f"error:{e}"
        out = await transform(data)
        await out_q.put(out)

async def consumer(in_q):
    results = []
    while True:
        item = await in_q.get()
        if item is None:
            break
        results.append(item)
    return results

async def main():
    raw_q = asyncio.Queue(maxsize=100)
    proc_q = asyncio.Queue()
    sem = asyncio.Semaphore(10)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(producer(raw_q, 200))
        for _ in range(5):
            tg.create_task(worker(raw_q, proc_q, sem))
        consumer_task = tg.create_task(consumer(proc_q))

    # After TaskGroup exit all tasks done
    await proc_q.put(None)
    results = consumer_task.result()
    print("Results count:", len(results))

asyncio.run(main())
```

Features: backpressure (queue), rate limiting (Semaphore), structured concurrency (TaskGroup), graceful sentinel shutdown.

---

## 27. Summary Cheat Sheet

| Need               | Use                                        |
| ------------------ | ------------------------------------------ |
| Run entry point    | `asyncio.run(main())`                      |
| Create task        | `asyncio.create_task(coro())` / TaskGroup  |
| Parallel I/O many  | `gather` or TaskGroup                      |
| Limit concurrency  | `Semaphore`                                |
| Backpressure       | `Queue` with maxsize                       |
| Cancel safe        | `try/except CancelledError` + cleanup      |
| Wrap blocking      | `await asyncio.to_thread(func)`            |
| CPU heavy          | `run_in_executor(ProcessPoolExecutor, fn)` |
| Timeout            | `await wait_for(coro, t)`                  |
| Rate limit + retry | Semaphore + loop with exponential backoff  |

---

## 28. Final Guidance

Start small: convert one I/O path to async, measure. Keep functions pure; isolate side effects. Prefer structured concurrency (TaskGroup) for reliability. Profile before optimizing. Combine with threads/processes only deliberately.

---

## 29. Comparison: Async IO vs Multithreading vs Multiprocessing

### 29.1 High-Level Summary

| Aspect                 | Async IO (`asyncio`)                              | Multithreading                                                         | Multiprocessing                                         |
| ---------------------- | ------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------- |
| Concurrency Model      | Single-threaded event loop; cooperative awaits    | Pre-emptive OS threads sharing memory                                  | Multiple OS processes; isolated memory                  |
| Best For               | Massive I/O-bound tasks (network sockets, APIs)   | Moderate I/O-bound with simpler imperative style; some mixed workloads | CPU-bound parallelism; isolation of heavy / unsafe code |
| CPU Parallelism        | No (unless offloading)                            | Blocked by GIL for pure Python                                         | Yes (each process has own GIL)                          |
| Memory Sharing         | Shared implicitly (same objects)                  | Shared; need locks                                                     | Separate; use IPC / shared memory                       |
| Overhead per Unit      | Very low (task objects)                           | Moderate (thread stacks, context switches)                             | High (process startup, serialization)                   |
| Failure Isolation      | Low (one uncaught error can bubble)               | Low (shared state corruption possible)                                 | Higher (crash contained to one process)                 |
| Cancellation / Timeout | First-class (`CancelledError`, `wait_for`)        | Manual (flags, events)                                                 | Manual (signals, sentinel messages)                     |
| Backpressure Mechanism | Await on `Queue.put()` / Semaphore                | Queue blocking / locks                                                 | Queue blocking / IPC semantics                          |
| Debug Complexity       | Await “stack” reasoning, tracing tasks            | Races, deadlocks, GIL contention                                       | Serialization errors, process lifecycle                 |
| Data Passing Cost      | In-memory references                              | In-memory references                                                   | Serialization / shared memory mapping                   |
| Typical Pitfalls       | Accidentally blocking loop, un-awaited coroutines | Deadlocks, GIL illusions, oversubscription                             | Pickling overhead, spawn recursion, high memory         |
| Tooling Maturity       | Growing (structured concurrency, TaskGroup)       | Mature, widely known                                                   | Mature but heavier                                      |

### 29.2 Choosing Strategy (Decision Tree)

1. Is workload primarily waiting on network / sockets / high-latency I/O? → Prefer Async IO.
2. Is workload pure CPU-bound Python code? → Multiprocessing (unless vectorized libs release GIL; then threading/async orchestrator ok).
3. Mixed: many I/O calls plus some small CPU transforms? → Async IO (maybe with `to_thread` / small process pool for spikes).
4. Need to integrate legacy blocking libraries and minimal refactor? → Use Threads (or wrap blocking pieces with `to_thread` while incrementally adopting async).
5. Need crash isolation / parallel heavy tasks? → Multiprocessing (optionally orchestrated by async loop via `run_in_executor`).

### 29.3 Latency vs Throughput Trade-offs

| Metric                     | Async IO                       | Threads                          | Processes               |
| -------------------------- | ------------------------------ | -------------------------------- | ----------------------- |
| Tail Latency (I/O)         | Often lowest when non-blocking | Good until thread count explodes | Higher (serialization)  |
| CPU Saturation Efficiency  | Weak alone                     | Weak for pure Python (GIL)       | Strong (cores utilized) |
| Context Switch Cost        | Very low (await state)         | Medium                           | High                    |
| Scaling to 10k Connections | Excellent                      | Poor (thread explosion)          | Impractical             |
| Scaling CPU to 8 cores     | Needs offload                  | Limited                          | Strong                  |

### 29.4 Code Shape Differences

Sequential style (threads) can appear simpler for small concurrency; async introduces `async/await` keywords but reduces need for explicit locks (no pre-emption mid-statement; only at awaits). Threads can mutate shared objects anytime, requiring defensive synchronization; async tasks only interleave at awaited points → easier local reasoning.

### 29.5 Memory & Serialization

-   Async / Threads: pass object references, almost zero overhead.
-   Processes: every argument / result of pool tasks is pickled (unless using shared memory or `fork` copy-on-write on Unix). Large Python object graphs pay a big tax → batch.

### 29.6 Error Propagation & Containment

| Concern               | Async IO                                | Threads                             | Processes                                  |
| --------------------- | --------------------------------------- | ----------------------------------- | ------------------------------------------ |
| Sibling Task Failure  | TaskGroup cancels siblings; else manual | Typically independent; must monitor | Parent can detect exit code / join failure |
| State Corruption Risk | Logical only (shared objects)           | High (races)                        | Low (isolation)                            |
| Restart Strategy      | Cancel & recreate tasks                 | Harder (thread reuse)               | Simple: restart process                    |

### 29.7 Cancellation & Shutdown

-   Async: propagate `CancelledError` with structured cleanup (finally blocks). Predictable.
-   Threads: cooperative via Event flags; risk of blocked system calls.
-   Processes: send sentinel / `terminate()`. Abrupt termination may leak resources.

### 29.8 Hybrid Patterns

| Pattern                             | Why Combine                                               |
| ----------------------------------- | --------------------------------------------------------- |
| Async orchestrator + Process pool   | Many I/O tasks plus CPU hot spots.                        |
| Async server + `to_thread` wrappers | Gradual migration from sync libs.                         |
| Thread supervising async loop       | Embedding event loop inside existing threaded app (rare). |

Example hybrid:

```python
import asyncio, math
from concurrent.futures import ProcessPoolExecutor

def cpu_part(n):
    return sum(math.sqrt(i) for i in range(n))

async def fetch_remote(x):
    await asyncio.sleep(0.05)
    return x * 2

async def pipeline(numbers):
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        # Fetch concurrently (I/O)
        fetched = await asyncio.gather(*(fetch_remote(n) for n in numbers))
        # CPU in parallel
        cpu_results = await asyncio.gather(*(
            loop.run_in_executor(pool, cpu_part, val*50_000) for val in fetched
        ))
    return cpu_results

async def main():
    out = await pipeline(range(10))
    print(len(out))

asyncio.run(main())
```

### 29.9 Performance Rule of Thumb Table

| Situation                                 | Prefer                    | Rationale                       |
| ----------------------------------------- | ------------------------- | ------------------------------- |
| 50k websocket clients                     | Async IO                  | Minimal per-connection overhead |
| Batch image processing                    | Processes                 | CPU parallel + isolation        |
| Burst of 500 HTTP calls then JSON parsing | Async IO (parsing inline) | Dominated by network wait       |
| Burst of 500 HTTP calls + heavy CPU parse | Async IO + process pool   | Split concerns                  |
| Legacy sync library cannot change         | Threads                   | Simpler adaptation              |
| Need deterministic isolation for sandbox  | Processes                 | Security boundary               |

### 29.10 Migration Guidance (Threads → Async)

1. Identify thread pools used only for I/O waiting.
2. Replace those producers/consumers with async tasks + `Queue`.
3. Leave CPU thread pools for now; later offload via `run_in_executor` from async world.
4. Convert blocking libs stepwise: wrap in `to_thread`, then swap for native async client.
5. Introduce TaskGroup for structured lifetimes.

### 29.11 Common Misconceptions Clarified

| Statement                          | Reality                                                          |
| ---------------------------------- | ---------------------------------------------------------------- |
| "Async is always faster."          | Only if there is significant I/O wait to overlap.                |
| "Threads are obsolete with async." | Threads remain vital for blocking or mixed sync libs.            |
| "Processes replace async."         | Processes solve CPU scaling, not I/O concurrency efficiency.     |
| "Async gives parallel CPU."        | Not without explicit offload to threads/processes / native code. |

### 29.12 Cheat Comparison Snapshot

| Need                      | Async         | Threads  | Processes |
| ------------------------- | ------------- | -------- | --------- |
| Massive connections       | ✅            | ❌       | ❌        |
| True CPU parallel         | ⚠️ (offload)  | ❌ (GIL) | ✅        |
| Low memory footprint      | ✅            | ⚠️       | ❌        |
| Simple incremental add    | ⚠️ (refactor) | ✅       | ⚠️        |
| Crash isolation           | ❌            | ❌       | ✅        |
| Fine-grained cancellation | ✅            | ⚠️       | ⚠️        |

### 29.13 When NOT to Use Async

-   Single, large CPU-bound batch job: just run synchronously or with processes.
-   Tiny script making 1–2 API calls: complexity overhead doesn’t pay off.
-   Performance-critical numeric loops already vectorized: async adds no gain.

---

In summary: Async IO shines at scaling I/O concurrency with minimal resource cost; threads ease integration with blocking code; processes unlock CPU parallelism and isolation. Mix intentionally—measure, don’t guess.

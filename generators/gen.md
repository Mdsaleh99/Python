# Generators in Python

## What is a Generator?

A **generator** is a special type of function in Python that allows you to iterate over a sequence of values, but instead of returning all the values at once, it yields them one at a time. This makes generators memory-efficient and useful for working with large data sets or streams.

## How to Create a Generator

You create a generator using a function with the `yield` keyword.

### Example 1: Simple Generator

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)
```

**Output:**
```
1
2
3
4
5
```

### Example 2: Generator Expression

You can also create a generator using a generator expression, similar to list comprehensions but with parentheses.

```python
squares = (x * x for x in range(5))
for square in squares:
    print(square)
```

**Output:**
```
0
1
4
9
16
```

## Why Use Generators?

- **Memory Efficient:** They generate values on the fly and do not store the entire sequence in memory.
- **Convenient:** Useful for reading large files, streaming data, or infinite sequences.

## Key Points

- Use `yield` instead of `return` to make a function a generator.
- Generators can be iterated only once.
- They are paused and resumed at each `yield`.

---

## More Concepts About Generators

### 1. Generator Functions vs Normal Functions

- **Normal functions** use `return` and return a single value, ending the function.
- **Generator functions** use `yield` and can yield multiple values, pausing after each yield and resuming from there.

### 2. The `next()` Function

You can manually get values from a generator using the `next()` function.

```python
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # Raises StopIteration
```

### 3. The `StopIteration` Exception

When a generator has no more values to yield, it raises a `StopIteration` exception.

### 4. Infinite Generators

Generators can be used to create infinite sequences.

```python
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_numbers()
for _ in range(5):
    print(next(gen))
```

**Output:**
```
1
2
3
4
5
```

### 5. Using Generators with `send()`

You can send values into a generator using the `send()` method.

```python
def echo():
    received = yield
    while True:
        received = yield received

gen = echo()
next(gen)           # Start the generator
print(gen.send(10)) # 10
print(gen.send(20)) # 20
```

### 6. Chaining Generators

Generators can be combined or chained together for complex data processing.

```python
def even_numbers(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

nums = range(10)
evens = even_numbers(nums)
for n in evens:
    print(n)
```

**Output:**
```
0
2
4
6
8
```
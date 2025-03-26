def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)


# The yield keyword in Python is used inside a function to create a generator instead of returning a value like return.    When a function has yield, it pauses execution and remembers where it left off. The next time the generator is called, it resumes from the last yield.
# Pauses execution, remembers state.  Returns multiple values one at a time.  Can be resumed from last yield
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of Positive number is: ", positive_number_count)

# The enumerate() function in Python is a built-in function that adds a counter to an iterable and returns it as an enumerate object. This object can then be used in loops to access both the index and the value of each item in the iterable

# iterable: Any object that supports iteration (e.g., list, tuple, string, set).
# start: An optional integer argument specifying the starting index for the counter. The default value is 0.

my_list = ['apple', 'banana', 'cherry']

for index, value in enumerate(my_list, start=1):
    print(f"Index: {index}, Value: {value}")



# zip() is a built-in function that aggregates elements from multiple iterables (like lists, tuples, or strings) into a single iterable of tuples. It pairs corresponding elements based on their position. 
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} and age is {age}")


# for else
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")
# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday
choice = int(input("Enter your age: "))

price = 12 if choice >= 18 else 8


"""
Python Data Types Examples
1. Number (int, float, complex)
2. String (str)
3. List (list)
4. Tuple (tuple)
5. Dictionary (dict)
6. Set (set)
7. Boolean (bool)
8. None Type (None)
"""

# is , == 

# 1️⃣ Number (int, float, complex)
# Integer (int)
x = 10  
y = -5  
z = 0  

# Float (decimal numbers)
a = 3.14  
b = -2.71  
c = 0.0  

# Complex Number
p = 2 + 3j  
q = -1 - 4j  
r = 5j  

# Octal  => base to the 8
0o20  # 16

# hex
0xFF  # 255

# binary
0b1000  # 8

oct(64)
hex(64)
bin(64)

int('64', 8)      # Octal 
int('64', 16)     # hex
int('10000', 2)   # binary


# ! ======================================================================================
# ! ======================================================================================


# 2️⃣ String (str)
# Using single or double quotes
name = "Alice"
greeting = 'Hello, World!'
quote = "Python is fun!"

# Multiline string
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""

# String with escape characters
path = "C:\\Users\\Admin\\Documents"


# ! ======================================================================================
# ! ======================================================================================



# 3️⃣ List (list) (Mutable & Ordered)
# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of mixed data types
mixed = ["Python", 3.14, True, [1, 2, 3]]

# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# 📌 List Comprehension in Python

# 1️⃣ Creating a list using list comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# 2️⃣ List comprehension with a condition (Even Numbers)
evens = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", evens)  # Output: [0, 2, 4, 6, 8]

# 3️⃣ Nested list comprehension (Multiplication Table)
table = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print("Multiplication Table:", table)

# 4️⃣ Converting lowercase to uppercase using list comprehension
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print("Uppercase Words:", uppercase_words)  # Output: ['APPLE', 'BANANA', 'CHERRY']

# 📌 Slicing in Python

# 5️⃣ Slicing a List
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Original List:", numbers)
print("First 3 elements:", numbers[:3])  # Output: [10, 20, 30]
print("Last 3 elements:", numbers[-3:])  # Output: [50, 60, 70]
print("Elements from index 1 to 4:", numbers[1:5])  # Output: [20, 30, 40, 50]
print("Every second element:", numbers[::2])  # Output: [10, 30, 50, 70]
print("Reversed List:", numbers[::-1])  # Output: [70, 60, 50, 40, 30, 20, 10]

# 6️⃣ Slicing a String
text = "PythonProgramming"
print("Original String:", text)
print("First 6 characters:", text[:6])  # Output: 'Python'
print("Last 6 characters:", text[-6:])  # Output: 'amming'
print("Alternate characters:", text[::2])  # Output: 'PtoPormig'
print("Reversed String:", text[::-1])  # Output: 'gnimmargorPnohtyP'

# 7️⃣ Slicing a Tuple
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Original Tuple:", numbers_tuple)
print("First 4 elements:", numbers_tuple[:4])  # Output: (1, 2, 3, 4)
print("Elements from index 3 to 6:", numbers_tuple[3:7])  # Output: (4, 5, 6, 7)
print("Reversed Tuple:", numbers_tuple[::-1])  # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1)



# ! ======================================================================================
# ! ======================================================================================


# 4️⃣ Tuple (tuple) (Immutable & Ordered)
# Tuple of numbers
coordinates = (10, 20, 30)

# Tuple with mixed data types
person = ("Alice", 25, "Engineer")

# Nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))



# ! ======================================================================================
# ! ======================================================================================



# 5️⃣ Dictionary (dict) (Key-Value Pairs, Mutable)
# Dictionary with string keys
person = {"name": "Alice", "age": 25, "city": "New York"}

# Dictionary with integer keys
marks = {101: 95, 102: 88, 103: 76}

# Dictionary with mixed keys
data = {1: "One", "two": 2, (3, 4): "Tuple Key"}



# ! ======================================================================================
# ! ======================================================================================




# 6️⃣ Set (set) (Unique, Unordered)
# Set of numbers
unique_numbers = {1, 2, 3, 4, 5}
# Sets
setone = {1, 2, 3, 4} 
setone | {1, 3} # Union The | operator returns a new set containing all unique elements from both sets.
setone & {1, 3} # Intersection  The & operator returns a new set containing only the common elements between both sets.
setone - {1, 2, 3, 4} # o/p => set() . no empty {} curly braces because empty {} for dictinory 'dict'
# Difference The '-' operator returns a new set with elements from setone that are not in the second set.

# Set of strings
fruits = {"apple", "banana", "cherry"}

# Set with mixed data types
mixed_set = {42, "hello", 3.14, (1, 2)}



# ! ======================================================================================
# ! ======================================================================================




# 7️⃣ Boolean (bool) (True or False)
# Simple boolean values
is_active = True
is_logged_in = False
has_permission = 5 > 3  # True

# Boolean as a result of comparison
is_equal = (10 == 20)  # False
is_greater = (50 > 30)  # True
is_empty = bool("")  # False (empty string is considered False)


# ! ======================================================================================
# ! ======================================================================================




# 8️⃣ None Type (None) (Represents "Nothing")
# Variable with no value
not_assigned = None

# Function returning None
def greet():
    print("Hello")
    return None

result = greet()  # result is None

# None in a dictionary
user_info = {"name": "Bob", "email": None, "age": 30}




# 📌 Class Example in Python

# Define a class named Person
class Person:
    # Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    # Method to display a greeting
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Method to check if the person is an adult
    def is_adult(self):
        return self.age >= 18

# Create objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 15)

# Access methods and attributes
person1.greet()  # Output: Hello, my name is Alice and I am 25 years old.
print("Is adult:", person1.is_adult())  # Output: True

person2.greet()  # Output: Hello, my name is Bob and I am 15 years old.
print("Is adult:", person2.is_adult())  # Output: False



class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self._radius = radius  # underscore means "private by convention"

    # 📍 Property to get the radius
    @property
    def radius(self):
        return self._radius

    # 📍 Property to get the area (computed like an attribute)
    @property
    def area(self):
        return Circle.pi * (self._radius ** 2)

    # 📍 Static method to describe a circle (doesn't use self or cls)
    @staticmethod
    def description():
        return "A circle is a shape with all points the same distance from its center."

# ✅ Using the class
c = Circle(5)

print("Radius:", c.radius)         # Output: Radius: 5
print("Area:", c.area)             # Output: Area: 78.53975
print(Circle.description())        # Output: A circle is a shape with all points the same distance from its center.


# A staticmethod in Python is a method that belongs to a class but doesn’t access or modify instance (self) or class (cls) attributes.    Can be called using the class name without creating an object.    Useful for utility/helper functions related to the class.

# The @property decorator in Python converts a method into a read-only attribute, allowing access like a variable instead of a method call. It is commonly used for encapsulation to control attribute access.
from decimal import Decimal
import math
import random

x = 2
y = 3
z = 4

int(2.23)
float(40)
'chai' + 'code'

x, y, z   # (2, 3, 4)

# +, -, *, **, /, %, //

repr('chai')
str('chai')
print('chai')
# repr() provides a string representation suitable for debugging,
# str() provides a more user-friendly string representation,
# print() is a function for outputting text or values to the console, typically using str() for the conversion.

math.floor(-3.5)
math.floor(3.6)

math.trunc(2.8)
math.trunc(-2.8)

2+1j
(2 + 1j) * 3 # (6 + 3j)


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

# bitwise operators    << , >> , | , & 

random.random()
random.randint(1, 100)

l1 = ["hi", "lemon", "hello", "mint"]
random.choice(l1)
random.shuffle(l1)
Decimal()

# Sets
setone = {1, 2, 3, 4}
setone | {1, 3}
setone & {1, 3}
setone | {1, 3}

setone - {1, 2, 3, 4} # o/p => set() . no empty {} curly braces because empty {} for dictinory 'dict'

True == 1
False == 0
True is 1  # False

True + 4  # 5
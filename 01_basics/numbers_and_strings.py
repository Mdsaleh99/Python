from decimal import Decimal
import math
import random
import sys

amount = 1_00_000 # one lakh (_)underscore for readability this ignores by python
print(amount) # o/p => 100000

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling    # upcasting
print(f"Total actions: {total_actions}")

# 0, None is are False value

# logical operators in python => and, or, not

print(sys.float_info)

x = 2
y = 3
z = 4

int(2.23)
float(40)
'chai' + 'code'

x, y, z   # (2, 3, 4)

# +, -, *, **, /, %, //,  // -> floor division,  / -> division

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
setone | {1, 3} # Union The | operator returns a new set containing all unique elements from both sets.
setone & {1, 3} # Intersection  The & operator returns a new set containing only the common elements between both sets.
setone - {1, 2, 3, 4} # o/p => set() . no empty {} curly braces because empty {} for dictinory 'dict'
# Difference The '-' operator returns a new set with elements from setone that are not in the second set.

True == 1
False == 0
True is 1  # False

True + 4  # 5


# ==================================== STRING  =============================================
label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")



masala_spices = ("cardamom", "cloves", "cinnamon")
(spice1, spice2, spice3) = masala_spices  # tuple destructring
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1   # behind the secene here python using tuple
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio # flipping the ratios
print(f"Ratio is G: {ginger_ratio} and C: {cadramom_ratio}")

print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}") # it is membership testing - "in" is the membership operator used to check if an element exists in a tuple or other collections.

# list methods
# insert(), sort(), reverse(), pop(), extend(), split() etc
# reverse() modifies the original list by reversing it in place.

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor  # operator overloading 
print(f"Liquid mix: {full_liquid_mix}")

strong_brew_1 = ["black tea"] * 3
print(f"String brew: {strong_brew_1}")

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")


raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print (f"Bytes: {raw_spice_data}")


# Dictionary
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

print(f"Is sugar in the order? {'sugar' in chai_order}") # membership testing - "in" is the membership operator used to check if an element exists in a tuple or other collections.

print(f"Order details (keys): {chai_order.keys()}") # return list
print(f"Order details (values): {chai_order.values()}") # return list
print(f"Order details (items): {chai_order.items()}") # return list of tuples


# collections
from collections import namedtuple

chai_profile = namedtuple("chaiProfile", ["flavor", "aroma"])

a = 5  
b = 5  
print(id(a) == id(b)) # o/p: True    because small integers are cached in python, so a and b point to the same memory location
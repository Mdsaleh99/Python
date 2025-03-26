import time

print("Chai is here")

username = "hitesh"
print(username)

# Check Notes Behind the scence of loops
# =====================================================================================

# >>> f = open('chai.py') 
# >>> f.readline()
# 'import time\n'
# >>> f.readline()        
# '\n'
# >>> f.readline()
# 'print("Chai is here")\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# 'username = "hitesh"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''
# >>> f.readline()
# ''
# >>> f.readline()
# ''


# =====================================================================================

# PS D:\chai-aur-python\04_iteration_tools> python
# Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> f = open('chai.py')
# >>> f.__next__()        
# 'import time\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'print("Chai is here")\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'username = "hitesh"\n'
# >>> f.__next__()
# 'print(username)\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


for line in open("chai.py"):
    print(line)
    # print(line, end='')

f = open('chai.py')
while True:
    line = f.readline()
    if not line: break
    print(line)
    # print(line, end='')


my_list = [1, 2, 3, 4]
I = iter(my_list)
# I => <list_iterator object at 0x0000027FA6490910>
I.__next__()

# >>> my_list = [1, 2, 3, 4]
# >>> I = iter(my_list)
# >>> I
# <list_iterator object at 0x0000027FA6490910>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x0000027FA6490910>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# we can use both __next__()  or  next()

"""
>>> f = open('chai.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
"""

"""
>>> my_list = [1, 2, 3, 4]
>>> iter(my_list) is my_list
False
>>> iter(my_list) is my_list.__iter__()
False
"""

# file ka jab refernce lete hai ek varible me toh oh ek apne aap me ek iterable object hai lekin list ka agar kisi memory refernce me uska naam diya hai toh oh uska iterable object nhi hai but oh uss list ka acutal object ka refernce hai 


"""
>>> range(0, 5)
range(0, 5)
>>> R = range(0, 5) 
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

# we can use both __next__()  or  next()
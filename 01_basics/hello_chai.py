import this
print("hello world")

def chai(n):
    print(n)
chai("lemon tea")


chai_one = "masala chai"
chai_two = "green tea"
chai_three = "mint tea"



username = "chai_lover"
print(dir(username))
print(dir(chai_one))



# >>> import hello_chai
# hello world
# lemon tea
# >>> hello_chai.chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'hello_chai' has no attribute 'chai_one'


# >>> from importlib import reload
# >>> reload(hello_chai) 
# hello world
# lemon tea
# <module 'hello_chai' from 'D:\\chai-aur-python\\01_basics\\hello_chai.py'>
# >>> hello_chai.chai_one
# 'masala chai'
# >>>
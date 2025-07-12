def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)


update_order()

# 'nonlocal' in Python is used in nested functions (a function defined inside another function) when you want to modify a variable that belongs to the outer function, but not to the global scope.

# Normal behavior (without nonlocal): If you try to change something in the small box, you'd likely just create a new item inside that smaller box. The item in the big box remains untouched.
# Using nonlocal: The nonlocal keyword is like a special instruction you put on a variable in the smaller box. It says, "Don't create a new item here. Go find the item with this name in the next biggest box (the outer function) and change that one instead!" 




chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
    kitchen()

front_desk()

print("Final global chai: ", chai_type)


# =======================================================
# from any function we not return Nothing it should give implictly returns None

def chai_report():
    return 100, 20, 10

sold, remaining, _ = chai_report() # here _ this means there are 3 values returning but one value we not using


# Types of functions
# 1. pure vs impure
# 2. recursive fuction
# 3. lambdas (Anonymous function) 


def pure_chai(cups):
    return cups * 10


total_chai = 0


# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups


def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    return flavor


print(chai_flavor.__doc__)
print(chai_flavor.__name__)

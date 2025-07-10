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
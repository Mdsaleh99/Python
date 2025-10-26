# MRO - (Method Resoultion Order)
# When you call a method on an object, Python needs to decide which class’s method to call first if multiple parent classes define the same method.

# ➡️ MRO tells Python the sequence of classes it should check to find that method.

# Python uses the C3 linearization algorithm to determine this order.

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(B, C):
    pass

cup = D()
print(cup.label) # o/p: B: Masala blend    because in class D we inheriting B first
print(D.__mro__)

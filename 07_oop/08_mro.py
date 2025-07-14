# MRO - (Method Resoultion Order)

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
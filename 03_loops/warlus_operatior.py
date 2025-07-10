
# := warlus operator
# The "walrus operator" in Python, introduced in Python 3.8, is formally known as an assignment expression. It is represented by the symbol :=.
# Purpose:
# The primary purpose of the walrus operator is to allow you to assign a value to a variable within an expression. This means you can compute a value, assign it to a variable, and then immediately use that variable within the same expression, such as in a conditional statement, a loop, or a list comprehension. 

# without warlus
# value = 13
# remainder = value % 5
# if remainder:
# print(f"Not divisible, remainder is {remainder}")


# with warlus operator
value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable {requested_size}")


# +=============================================
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0,10),
}

for user in users:
    percent, fixed = discounts.get(user ["coupon"], (0,0))
    discount = user ["total"] * percent + fixed
    print(f"{user ["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")
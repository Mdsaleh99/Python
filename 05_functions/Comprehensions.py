"""
    Comprehensions:
    Comprehensions are a concise way to create
    lists,
    sets,
    dictionaries,
    or generators
    in Python using a single line of code.

    Types of Comprehensions:
    1. List
    2. Set
    3. Dictornary
    4. Generator

    syntax of Comprehensions:
    1. List -> [expression for item in iterable if condition]
    2. Set -> {expression for item in iterable if condition}
    3. Dict -> {expression for item in iterable if condition}  for dict expression should be key:value pair
    4. Generator -> (expression for item in iterable if condition)  Generator used for saving the memory

    [ x for x in items]
    make entire list in memory

    (x for x in items)
    like a stream
"""
# in all Comprehensions we have to read first for loop and then expression
# 1. List Comprehensions
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)


# 2. Set Comprehensions
favourite_chais = [
    "Masala Chai", 
    "Green",
    "Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_chai)


# 3. Dict Comprehensions
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)


# 4. Generator Comprehensions
# it is very memory effeicent code
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
total_cups = (sale for sale in daily_sales if sale > 5)

print(total_cups) # o/p -> <generator object <genexpr> at 0x104f26b50>
# total_cups = sum(sale for sale in daily_sales if sale > 5)
# print(total_cups) # o/p -> 61
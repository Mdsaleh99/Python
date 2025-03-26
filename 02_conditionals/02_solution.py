age = 22
day = "Wednesday"

price = 12 if age >= 18 else 8  # price me ya toh 12 aayega ya 8 aayega
print(price)

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)
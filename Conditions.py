# 1

temperature = 21
if temperature > 21:
    print("It's a warm day") # False
elif temperature < 21:
    print("It's a cold day") # False
else:
    print("It's a lovely day") # Will print -> It's a lovely day


#2

price = 1000000
salary = 120000
if price / salary > 8:
    print("We can give you credit in 10% per year") # True -> We can give you credit in 10% per year
elif price / salary < 8:
    print("We can give you credit in 20% per year")
else:
    print("We can give you credit in 15% per year")
    
#3

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")  # Down payment: $100000.0

#1. We can input integer and output our entered integer, 

age = int(input("Age: "))
print(age)  # 30 -> 30

#1.1 but if the value is string, it'll shows value error

age = int(input("Age: "))
print(age)  # L -> ValueError: invalid literal for int() with base 10: 'L'


#2 We can put this code to "try" block and into "expect" block write 'Invalid value' if input isn't integer

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print('Invalid value')   
    
"""
1. 30 -> 30
2. L -> Invalid value


#3. We can add another errors. For example we cannot divide to zero

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')   # 0 -> Age cannot be 0.
    
    

"""

Conditional expressions provide the functionality of if statements while using less code.
They shouldn't be overused, as they can easily reduce readability, but they are often useful when assigning variables.
Conditional expressions are also known as applications of the ternary operator.

"""

# 1

a = 7
b = 1 if a >= 5 else 42
print(b)                            # 1

"""

The ternary operator checks the condition and returns the corresponding value.
In the example above, as the condition is true, b is assigned 1. 
If a was less than 5, it would have been assigned 42.

"""

# 2

status = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

# The ternary operator is so called because, unlike most operators, it takes three arguments.

b=1 if 2+2==5 else 2
print(b)

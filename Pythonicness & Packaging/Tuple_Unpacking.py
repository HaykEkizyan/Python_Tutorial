# Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.

# 1

numbers = (1, 2, 3)
a, b, c = numbers
print(a)                        # 1
print(b)                        # 2
print(c)                        # 3

# This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side
# forms the tuple (b, a) which is then unpacked.




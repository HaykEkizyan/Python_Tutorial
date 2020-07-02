# Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.

# 1

numbers = (1, 2, 3)
a, b, c = numbers
print(a)                        # 1
print(b)                        # 2
print(c)                        # 3

# This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side
# forms the tuple (b, a) which is then unpacked.

# 1.1

x,y=[1,2]
x,y=y,x
print(y)                        # 1

# A variable that is prefaced with an asterisk (*)
# takes all values from the iterable that are left over from the other variables.

# 2

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)                                    # 1
print(b)                                    # 2
print(c)                                    # [3, 4, 5, 6, 7, 8]
print(d)                                    # 9

# 2.1

a, b, c, d, *e, f, g = range(20)
print(len(e))                               # 14

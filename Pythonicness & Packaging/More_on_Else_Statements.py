"""

The else statement is most commonly used along with the if statement,
but it can also follow a for or while loop, which gives it a different meaning.
With the for or while loop, the code within it is called if the loop finishes normally
(when a break statement does not cause an exit from the loop).

"""

# 1

for i in range(10):
    if i == 999:
        print(1)
        break
else:
    print("Unbroken 1")             # Unbroken 1

for i in range(10):
    if i == 5:
        print(1)                    # 1
        break
else:
    print("Unbroken 2")

# The first for loop executes normally, resulting in the printing of "Unbroken 1".
# The second loop exits due to a break, which is why it's else statement is not executed.

# 1.1

for i in range(10):
    if i > 5:
        print(i)                    # 6
        break
else:
    print("7")


# The else statement can also be used with try/except statements.
# In this case, the code within it is only executed if no error occurs in the try statement.

# 2

try:
    print(1)                        # 1
except ZeroDivisionError:
    print(2)
else:
    print(3)                        # 3

try:
    print(1/0)
except ZeroDivisionError:
    print(4)                        # 4
else:
    print(5)



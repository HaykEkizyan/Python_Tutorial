"""                                                             Magic Methods

Magic methods are special methods which have double underscores at the beginning and end of their names.
They are also known as dunders.
So far, the only one we have encountered is __init__, but there are several others.
They are used to create functionality that can't be represented as a normal method.

One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such as + and * to be used on them.
An example magic method is __add__ for +.

"""

#1

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)                                     # 8
print(result.y)                                     # 16

"""

The __add__ method allows for the definition of a custom behavior for the + operator in our class.
As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
Once it's defined, we can add two objects of the class together.

"""

"""

More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
There are equivalent r methods for all magic methods just mentioned.

"""

class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

"""
spam
============
Hello world!
"""

"""

In the example above, we defined the division operation for our class SpecialString.

"""


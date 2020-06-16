"""

 Properties provide a way of customizing access to instance attributes.
 They are created by putting the property decorator above a method, which means when the instance attribute 
with the same name as the method is accessed, the method will be called instead.
 One common use of a property is to make an attribute read-only.
 
"""

#1 Example

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return 1

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)                                        # 1
pizza.pineapple_allowed = True                                        # AttributeError: can't set attribute

#1.1 Example

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False

Hayk = Person(30)
print(Hayk.isAdult)                                                   # True

"""

 Properties can also be set by defining setter/getter functions.
 The setter function sets the corresponding property's value.
 The getter gets the value.
 To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
 The same applies to defining getter functions.
 






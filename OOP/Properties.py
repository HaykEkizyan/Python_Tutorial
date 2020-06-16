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

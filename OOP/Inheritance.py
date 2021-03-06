 """                                                             Inheritance
                                                              
Inheritance provides a way to share functionality between classes.
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways (only Dog might have the method bark), 
 they are likely to be similar in others (all having the attributes color and name).   
This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
To inherit a class from another class, put the superclass name in parentheses after the class name.
"""
#1

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof")

hachi = Dog("Hachi", "brown")
print(hachi.color)                                            # brown
hachi.bark()                                                  # Woof

"""
A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
In the example above, Animal is the superclass, Dog is the subclass.
If a class inherits from another with the same attributes or methods, it overrides them.
"""
#1.1

class A:
    def method(self):
        print(1)

class B(A):
    def method(self):
        print(2)

B().method()                                                  # 2

#1.2  Indirect Inheritance

class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()                                                    # A method
c.another_method()                                            # B method
c.third_method()                                              # C method

# However, circular inheritance is not possible.

#1.3

class A:
    def a(self):
        print(1)
class B(A):
    def a(self):
        print(2)
class C(B):
    def c(self):
        print(3)

c = C()
c.a()                                                         # 2

#1.4

class People:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Hi from " + self.name)

class Person(People):
    pass

person_hayk = Person("Hayk")
person_hayk.talk()                                            # Hi from Hayk

#2 super
"""
The function super is a useful inheritance-related function that refers to the parent class. 
It can be used to find the method with a certain name in an object's superclass.
"""
#2.1

class A:
    def spam(self):
        print(1)
class B(A):
    def spam(self):
        print(2)                                               # 2
      # super().spam()
B().spam()                                                   

#2.2

class A:
    def spam(self):
        print(1)
class B(A):
    def spam(self):
        print(2)                                              # 2
        super().spam()                                        # 1  """ super().spam() calls the spam method of the superclass."""
B().spam()


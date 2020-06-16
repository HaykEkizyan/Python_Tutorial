"""

 A key part of object-oriented programming is encapsulation, which involves packaging of related variables and 
functions into a single easy-to-use object - an instance of a class.
 A related concept is data hiding, which states that implementation details of a class should be hidden, and 
a clean standard interface be presented for those who want to use the class. 
 In other programming languages, this is usually done with private methods and attributes, 
which block external access to certain methods and attributes in a class.
 The Python philosophy is slightly different. It is often stated as "we are all consenting adults here", 
meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. 
Hence there are no ways of enforcing a method or attribute be strictly private.
 However, there are ways to discourage people from accessing parts of a class, such as by denoting that 
it is an implementation detail, and should be used at their own risk.

"""

"""

 Weakly private methods and attributes have a single underscore at the beginning.
 This signals that they are private, and shouldn't be used by external code. 
However, it is mostly only a convention, and does not stop external code from accessing them.
 Its only actual effect is that from module_name import * won't import variables that start with a single underscore.
 
"""

#1 Example

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    def push(self, value):
        self._hiddenlist.insert(0, value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)                                           # Queue([1, 2, 3])
queue.push(0)
print(queue)                                           # Queue([0, 1, 2, 3])
queue.pop()
print(queue)                                           # Queue([0, 1, 2])
print(queue._hiddenlist)                               # [0, 1, 2]

"""

In the code above, the attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.
The __repr__ magic method is used for string representation of the instance.

"""

"""

 Strongly private methods and attributes have a double underscore at the beginning of their names. 
This causes their names to be mangled, which means that they can't be accessed from outside the class.
 The purpose of this isn't to ensure that they are kept private, but to avoid bugs 
if there are subclasses that have methods or attributes with the same names.
 Name mangled methods can still be accessed externally, but by a different name. 
The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.

#2 Example

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)
s = Spam()
s.print_egg()                                         # 7
print(s._Spam__egg)                                   # 7
print(s.__egg)                                        # AttributeError: 'Spam' object has no attribute '__egg'



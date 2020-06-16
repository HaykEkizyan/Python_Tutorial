"""

 The lifecycle of an object is made up of its creation, manipulation, and destruction.
 The first stage of the life-cycle of an object is the definition of the class to which it belongs.
The next stage is the instantiation of an instance, when __init__ is called.
Memory is allocated to store the instance.
Just before this occurs, the __new__ method of the class is called.
This is usually overridden only in special cases.
 After this has happened, the object is ready to be used.
 Other code can then interact with the object, by calling functions on it and accessing its attributes.
 Eventually, it will finish being used, and can be destroyed.
 
"""





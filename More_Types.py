#1 It is similar to null in other programming languages.

print(None == None)  #  True

#1.1 Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.

print(None)  #  None

#1.2 The None object is returned by any function that doesn't explicitly return anything else.

def some_func():
    print('Hi!')
var = some_func()
print(var)

"""
Hi!
None
"""

#1.3 

foo = print()
if foo == None:
    print(1)
else:
    print(2)  #  1
    

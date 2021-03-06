#1

Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
They can be created using functions and the yield statement.
The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller 
 without destroying local variables.

#1.1

def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
"""
5
4
3
2
1
"""

#1.2 

Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
In fact, they can be infinite!

def infinite_sevens():
    while True:
        yield 7
#       break                       #  7 - with break
for i in infinite_sevens():
    print(i)                        #  infinite 7...
    
In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.


#1.3

Finite generators can be converted into lists by passing them as arguments to the list function.

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))             #  [0, 2, 4, 6, 8, 10]

Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, 
which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been generated 
before we start to use them.

def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word
print(list(make_word()))             #  ['s', 'sp', 'spa', 'spam']




#2

Decorators provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you don't want to modify.

def decor(func):
    def wrap():
        print("===========")
        func()
        print("=============")
    return wrap
def print_text():
    print("Hello world!")
    
decorated = decor(print_text())    # cahnged with line 90
decorated()

We defined a function named decor that has a single parameter func. Inside decor, we defined a nested function named wrap. 
The wrap function will print a string, then call func(), and print another string. The decor function returns the wrap function as its result.
We could say that the variable decorated is a decorated version of print_text - it's print_text plus something.
In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always 
got our "plus something" version of print_text.
This is done by re-assigning the variable that contains our function:

print_text = decor(print_text)
print_text()                        # cahnged with line 79

Full:

def decor(func):
    def wrap():
        print("===========")
        func()
        print("=============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)
print_text()                        
"""
===========
Hello world!
=============
"""

#2.1 

Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
If we are defining a function we can "decorate" it with the @ symbol like:

@decor
def print_text():
    print("Hello world!")
    
This will have the same result as the above code.

def print_text():
    print("Hello world!")
print_text = decor(print_text)


A single function can have multiple decorators.


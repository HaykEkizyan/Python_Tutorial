Functional programming is a style of programming that (as the name suggests) is based around functions.
A key part of functional programming is higher-order functions. 
 Higher-order functions take other functions as arguments, or return them as results.
 
# 1

def apply_twice(func, arg):   # arg -> 0
    return func(func(arg))

def add_five(x):    # func -> add_five
    return x + 5

print(apply_twice(add_five, 0))    #  10

1.1

def apply_twice(func, arg):   # arg -> 10
    return func(func(arg))

def add_five(x):    # func -> add_five
    return x + 5

print(apply_twice(add_five, 10))    #  20

1.2

def test(func, arg):   # arg -> 3
    return func(func(arg))

def mult(x):    # func -> mult
    return x * x

print(test(mult, 3))    #  81


#2 Pure Functions
Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.

#2.1 

def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)

print(pure_function(2, 4))    #  1.25

#2.2  It's a pure function

def func(x):
  y = x**2
  z = x + y
  return z
  
  
#2.3  It' not a pure function

some_list = []

def impure(arg):
  some_list.append(arg)
  
  
Using pure functions has both advantages and disadvantages.
Pure functions are:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the 
  function of that input is needed, reducing the number of times the function is called. This is called memoization.
- easier to run in parallel.

The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O, 
 since this appears to inherently require side effects.
They can also be more difficult to write in some situations.



#3 Lambdas
Creating a function normally (using def) assigns it to a variable automatically.
This is different from the creation of other objects - such as strings and integers - which can be created on the fly, 
without assigning them to a variable. 
The same is possible with functions, provided that they are created using lambda syntax. 
Functions created this way are known as anonymous.
This approach is most commonly used when passing a simple function as an argument to another function. 
The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, 
and the expression to evaluate and return.

Lambda functions get their name from lambda calculus, which is a model of computation invented by Alonzo Church.

#3.0

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)


Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression - usually equivalent to a single line of code.


#3.1.0 named function

def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))                    #  0

#3.1.1 lambda

print((lambda x: x**2 +5*x +4) (-4))     #  0

print((lambda x: x*x) (8))               #  64

#3.1.2 Lambda functions can be assigned to variables, and used like normal functions.

double = lambda x: x * 2
print(double(7))                         #  14

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))                 #  13

a = (lambda x: x * (x + 1))(6)
print(a)                                 #  42 

#4 Map & Filter
The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables).

#4.1 Map
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

def add_five(x):
    return x + 5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))   #  To convert the result into a list, we used list explicitly.
print(result)                        #  [16, 27, 38, 49, 60]

#4.1.1  We could have achieved the same result more easily by using lambda syntax.

nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)                  #  [16, 27, 38, 49, 60]

nums = [11, 22, 33]
a = list(map(lambda x: x*2, nums))
print(a)                       #   [22, 44, 66]


#4.2  Filter
The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)                                     #  [22, 44]

nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x < 5, nums))
print(res)                                     #  [1, 2, 3, 0]




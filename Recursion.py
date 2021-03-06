Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference - functions calling themselves. 
It is used to solve problems that can be broken up into easier sub-problems of the same type.

A classic example of a function that is implemented recursively is the factorial function, 
 which finds the product of all positive integers below a specified number.
For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, 
 notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.
Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials.

Below is a recursive implementation of the factorial function.

# 1 

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(5))                   #   120

The base case acts as the exit condition of the recursion.

#2

Recursive functions can be infinite, just like infinite while loops. These often occur when you forget to implement the base case.
Below is an incorrect version of the factorial function. It has no base case, so it runs until the interpreter runs out of memory and crashes.

def factorial(x):
    return x * factorial(x - 1)
print(factorial(5))               #   RecursionError: maximum recursion depth exceeded

#2.1

def sum_to(x):
    return x + sum_to(x - 1)
print(sum_to(5))                  #   RecursionError: maximum recursion depth exceeded


#2.2

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)
def is_odd(x):
    return not is_even(x)
print(is_odd(17))                 #   True
print(is_even(23))                #   False


#2.3

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
print(fib(4))                              #  5

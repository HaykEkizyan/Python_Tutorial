"""

 This is an example of solving a problem, the requirements for which are presented below.

 Let's call a list beautiful if its first element is equal to its last element, or if a list is empty. Given a list a, 
your task is to chop off its first and its last element until it becomes beautiful. 
Implement a function that will make the given a beautiful as described, and return the resulting list as an answer.

"""

def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a_, *res, a = res
    return res
print(listBeautifier([3, 4, 2, 4, 38, 4, 5, 3, 2]))        # [4, 38, 4]
print(listBeautifier([1, 4, -5]))                          # [4]


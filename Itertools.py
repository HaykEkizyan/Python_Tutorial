The module itertools is a standard library that contains several functions that are useful in functional programming.
One type of function it produces is infinite iterators.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable (for instance a list or string).
The function repeat repeats an object, either infinitely or a specific number of times.

from itertools import count

#1 count

for i in count(3):
    print(i)        #  3 4 5 6 7
    if i >= 7:
        break

#1.1 count

for i in count(3):
    print(i)        # 3
    if i >= 1:
        break

#2 cycle

from itertools import cycle

for i in cycle("5"):
    print(i)        # 5
    break           # without break it will be infinite
    
    
#3 repeat

from itertools import repeat

for i in repeat("5"):
    print(i)        # 5
    break           # without break it will be infinite
    
    
#4 

There are many functions in itertools that operate on iterables, in a similar way to map and filter.

#4.1

accumulate - returns a running total of values in an iterable.

from itertools import accumulate
nums = list(accumulate(range(5)))
print(nums)                             # [0, 1, 3, 6, 10]
nums = list(accumulate(range(9)))
print(nums)                             # [0, 1, 3, 6, 10, 15, 21, 28, 36]


#4.2

takewhile - takes items from an iterable while a predicate function remains true.

from itertools import takewhile, accumulate
nums = list(accumulate(range(9)))
print(list(takewhile(lambda x: x <= 13, nums)))         # [0, 1, 3, 6, 10]

from itertools import takewhile
nums = [2, 4, 3, 6, 7, 9, 8, 6, 4]
a = takewhile(lambda x: x % 2 == 0, nums)
print(list(a))                                          # [2, 4]


#4.3

chain - combines several iterables into one long one.

from itertools import chain
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list = list(chain(['foo', 'bar'], cmd, numbers))
print(my_list)                                          # ['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]



#5 product, permutations

There are also several combinatoric functions in itertool, such as product and permutation.
These are used when you want to accomplish a task with all possible combinations of some items.

#5.1

from itertools import product, permutations
letters = ("A", "B")
print(list(product(letters, range(2))))                 # [('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(permutations(letters)))                      # [('A', 'B'), ('B', 'A')]

#5.2

from itertools import product
a = {1, 2}
print(list(product(range(3), a)))                       # [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]            
print(len(list(product(range(3), a))))                  # 6



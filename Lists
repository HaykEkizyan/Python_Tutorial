#1

arr = [1, 2, "fruit", "water"]
print(arr[3])  #  water


#2

arr = [1, 2, "fruit", "water"]
print(arr[1])  #  2


#3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item) 
       """
        1
        2
        3
        4
        5
        6
        7
        8
        9
       """

#4 If the first number in a slice is omitted, it is taken to be the start of the list. If the second number is omitted, ...

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])
"""
[0, 1, 4, 9, 16, 25, 36]
[49, 64, 81]
"""

#5 List slices can also have a third number, representing the step, to include only alternate values in the slice.
   [2:8:3] will include elements starting

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:8:3])
print(squares[2::3])
print(squares[::2])
"""
[4, 25]
[4, 25, 64]
[0, 4, 16, 36, 64]
"""


#6 Negative values can be used in list slicing (and normal list indexing). When negative values are used for the first and 
   second values in a slice (or a normal index), they count from the end of the list.
   If a negative value is used for the step, the slice is done backwards.
   Using [::-1] as a slice is a common and idiomatic way to reverse a list.
   
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1::4])
print(squares[3:-1])
print(squares[::-1])
"""
[1, 25, 81]
[9, 16, 25, 36, 49, 64]
[81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
"""


#7 List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
   List comprehensions are inspired by set-builder notation in mathematics.
   
cubes = [i**3 for i in range(5)]
print(cubes)   #  [0, 1, 8, 27, 64]


#8 A list comprehension can also contain an if statement to enforce a condition on values in the list.

cubes = [i**2 for i in range(10) if i**2 % 2 == 0]
print(cubes)   #  [0, 4, 16, 36, 64]


#7.1 

cubes = [i for i in range(20) if i % 3 == 0]
print(cubes)    #   [0, 3, 6, 9, 12, 15, 18]



#8 List Functions

#8.1 Often used in conditional statements, all and any take a list as an argument, and return True if all 
     or any (respectively) of their arguments evaluate to True (and False otherwise).
     
nums = [55, 44, 33, 22, 11]
if all([i > 10 for i in nums]):
    print("All larger than 5")            #  All larger than 5

#8.1.1

nums = [55, 44, 33, 22, 11]

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")         #  At least one is even
    
#8.2 The function enumerate can be used to iterate through the values and indices of a list simultaneously.

nums = [55, 44, 33, 22, 11]
for v in enumerate(nums):
    print(v)                             
"""
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
"""





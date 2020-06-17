"""
Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.

Trying to reassign a value in a tuple causes a TypeError. 
  >>>
  TypeError: 'tuple' object does not support item assignment
  >>>
Like lists and dictionaries, tuples can be nested within each other.

An empty tuple is created using an empty parenthesis pair.  -> tpl = ()

Tuples are faster than lists, but they cannot be changed.

"""

#1

numbers = (1, 2, 3)
print(numbers.count(3))   # 1
print(numbers.index(3))   # 2
print(numbers.clear())    # 'tuple' object has no attribute 'clear'


# 2 

"""
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
"""

# you can write it like

"""
coordinates = (1, 2, 3)
x, y, z = coordinates
"""

#3

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)   #  1


#4

coordinates = (1, 2, 3)
x, y, z = coordinates
print((x, y, z) == (1, 2, 3))   # True


#5 square brackets

coordinates = [1, 2, 3]
x, y, z = coordinates
print([x, y, z] == [1, 2, 3])   # True


#6  change to parentheses - line 50, 1st part

coordinates = [1, 2, 3]
x, y, z = coordinates
print((x, y, z) == [1, 2, 3])    # False


#7  change to parentheses - line 57

coordinates = [1, 2, 3]
x, y, z = coordinates
print((x, y, z) == (1, 2, 3))    # True


#8 Tuples can be created without the parentheses, by just separating the values with commas.

words = "spam", "eggs", "sausages"
print(words[0])  #  spam



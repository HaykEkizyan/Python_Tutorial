Sets are data structures, similar to lists or dictionaries. They are created using curly braces, or the set function. 
They share some functionality with lists, such as the use of in to check whether they contain a particular item.

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
print(3 in num_set)                               #  True
print("spam" not in word_set)                     #  False

To create an empty set, you must use set(), as {} creates an empty dictionary.

#1

letters = {"a", "b", "c", "d"}
if "e" not in letters:
    print(1)
else:
    print(2)                                      # 1
    

#2

Sets differ from lists in several ways, but share several list operations such as len.
They are unordered, which means that they can't be indexed.
They cannot contain duplicate elements.
Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
Instead of using append to add to a set, use add.
The method remove removes a specific element from a set; pop removes an arbitrary element.

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)                            # {1, 2, 3, 4, 5, 6}
nums.remove(3)
print(nums)                            # {1, 2, 4, 5, 6}
nums.pop()
print(nums)                            # {2, 4, 5, 6}
print(len(nums))                       # 4
nums.add(7)
nums.add(1)
print(nums)                            # {2, 1, 4, 5, 6, 7}

!!!! Basic uses of sets include membership testing and the elimination of duplicate entries.

#3

Sets can be combined using mathematical operations.


#3.1  The union operator | combines two sets to form a new one containing items in either.

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
union = first | second
print(union)                            # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#3.2  The intersection operator & gets items only in both.

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
union = first & second
print(union)                            # {4, 5, 6}

#3.3  The difference operator - gets items in the first set but not in the second.

#3.3.1

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
union = first - second
print(union)                            # {1, 2, 3}

#3.3.2

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
union = second - first
print(union)                            # {8, 9, 7}

#3.4  The symmetric difference operator ^ gets items in either set, but not both.

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
union = second ^ first
print(union)                            # {1, 2, 3, 7, 8, 9}



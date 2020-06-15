#1 

customer = {
    "name": "Hayk Ekizyan",
    "age": 30,
    "is_verified": True
}
print(customer["name"])                   #  Hayk Ekizyan
print(customer.get("name"))               #  Hayk Ekizyan
customer["birthdate"] = "Dec 7 1989"
print(customer["birthdate"])              #  Dec 7 1989


#2 When the key does not exist

primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255]
}

print(primary.get("red")) # [255, 0, 0]
print(primary["yellow"])  # KeyError: 'yellow'

#2.1 

test = { }
print(test[0])  # KeyError: 0


#2.3 Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be changed.

bad_dict = {
    [1, 2, 3]: "one two three"
}
print(bad_dict[[1, 2, 3]])  # TypeError: unhashable type: 'list'


#3 We can change values 

squares = {
    1: 1,
    2: 4,
    3: "error",
    4: 16
}
squares[8] = 64
squares[3] = 9
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 8: 64}


#4 To determine whether a key is in a dictionary...

nums = {
    1: "one",
    2: "two",
    3: "three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)  
"""
True
False
True
"""

#5 "get" method. if the key is not found in the dictionary it returns another specified value instead...

pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True"
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
print(pairs.get(1 in pairs))

"""
[2, 3, 4]
None
not in dictionary
False
"""



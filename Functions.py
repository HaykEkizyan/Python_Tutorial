#1. 

def user():
    print("Good afternnon")
    print("Good evening")
print("Good morning")
user()
print("Good night")

"""
Good morning
Good afternnon
Good evening
Good night
"""

#2. With parameters

def user(name):
    print("Good afternnon " + name)
    print("Good evening " + name)
print("Good morning")
user("Hayk")
print("Good night")

"""
Good morning 
Good afternnon Hayk
Good evening Hayk
Good night
"""

#3. 

def user(name):
    print("Good afternnon " + name)
    print(f"Good evening {name}")
print("Good morning")
user("Hayk")
user("Anna")
print("Good night")

"""
Good morning
Good afternnon Hayk
Good evening Hayk
Good afternnon Anna
Good evening Anna
Good night
"""

#4. With two arguments

def user(first_name, last_name):
    print("Good afternnon " + first_name + " " + last_name)
    print(f"Good evening {first_name} {last_name}")
print("Good morning")
user("Hayk", "Ekizyan")
user("Anna", "Grigoryan")
print("Good night")

"""
Good morning
Good afternnon Hayk Ekizyan
Good evening Hayk Ekizyan
Good afternnon Anna Grigoryan
Good evening Anna Grigoryan
Good night
"""

#5. If we need to change the arguments places

def user(first_name, last_name):
    print("Good afternnon " + first_name + " " + last_name)
    print(f"Good evening {first_name} {last_name}")
print("Good morning")
user(last_name="Ekizyan", first_name="Hayk")
user("Anna", last_name="Grigoryan")
print("Good night")

"""
Good morning
Good afternnon Hayk Ekizyan
Good evening Hayk Ekizyan
Good afternnon Anna Grigoryan
Good evening Anna Grigoryan
Good night
"""

#5.1 Will be SyntaxError

def user(first_name, last_name):
    print("Good afternnon " + first_name + " " + last_name)
    print(f"Good evening {first_name} {last_name}")
print("Good morning")
user(first_name="Ekizyan", "Hayk")    # error in this line
user("Anna", last_name="Grigoryan")
print("Good night")

"""
user(first_name="Ekizyan", "Hayk")
                               ^
SyntaxError: positional argument follows keyword argument
"""

#6.  return staement

def square(number):
    return number ** number
print(square(3))  # 27

#6.1

def square(number):
    return number ** number
    print(square(3))   # no output

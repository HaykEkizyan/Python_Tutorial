#1

fruits = "apple, banana, orange"
print(fruits.replace('banana', 'kiwi'))
print('kiwi' in fruits)
print(fruits)  
"""
apple, kiwi, orange
False
apple, banana, orange
"""


#2 split() -> returns text you have entered in string type

message = input("> ")
words = message.split(" ")
print(words)   # 456 -> ['456']


#3 String formatting provides a more powerful way to embed non-strings within strings. 
   String formatting uses a string's format method to substitute a number of arguments in the string.
   Each argument of the format function is placed in the string at the corresponding position, which is 
   determined using the curly braces { }.
   
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)  # Numbers: 4 5 6


#3.1 

print("{0}{1}{0}".format("abra", "cad"))   #  abracadabra


#3.2 String formatting can also be done with named arguments.

a = '{x}, {y}'.format(x = 5, y = 12)
print(a)    #   5, 12


#3.3 

str = "{c}, {b}, {a}".format(a = 5, b = 9, c = 7)
print(str)   # 7, 9, 5



#4 String Functions - Python contains many useful built-in functions and methods to accomplish common tasks.

#4.1 join - joins a list of strings with another string as a separator.

print(";".join(["spam", "eggs", "ham"]))   #  spam;eggs;ham

#4.2 replace - replaces one substring in a string with another.

print("Hello ME".replace("ME", "world"))   #  Hello world
print("Hello ME".replace("Me", "world"))   #  Hello ME

#4.3 startswith and endswith - determine if there is a substring at the start and end of a string, respectively.

print("This is a sentence".startswith("This is"))    #   True
print("This is a sentence".startswith("This was"))   #   False

print("This is a sentence".endswith("This is"))      #   False
print("This is a sentence".endswith("ence"))         #   True
print("This is a sentence".endswith("Sentence"))     #   False

#4.4 To change the case of a string, you can use lower and upper.

print("This is a sentence".upper())   #   THIS IS A SENTENCE
print("This is a sentence".lower())   #   this is a sentence

#4.5 The method split is the opposite of join, turning a string with a certain separator into a list.

print("spam, eggs, ham".split(","))  #   ['spam', ' eggs', ' ham']






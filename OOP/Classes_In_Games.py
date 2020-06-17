"""

 Object-orientation is very useful when managing different objects and their relations.
 That is especially useful when you are developing games with different characters and features.
 
 Let's look at an example project that shows how classes are used in game development.
 The game to be developed is an old fashioned text-based adventure game.
 Below is the function handling input and simple parsing.
 
"""

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unkonown verb {}". format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))
def say(noun):
    return 'You said "{}"'. format(noun)
verb_dict = {
    "say": say,
}

while True:
    get_input()
    
"""
: say 123
You said "123"
: test
Unkonown verb test
: ttt
Unkonown verb ttt
: .
Unkonown verb .
: say Hello!
You said "Hello!"
: say Goodbye!
You said "Goodbye!"
"""

"""

The code above takes input from the user, and tries to match the first word with a command in verb_dict. 
If a match is found, the corresponding function is called.

"""

"""

The next step is to use classes to represent game objects.

"""

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

class Goblin(GameObject):
    class_name = "goblin"
    desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)
     
     
"""

We created a Goblin class, which inherits from the GameObjects class.
We also created a new function examine, which returns the objects description.
Now we can add a new "examine" verb to our dictionary and try it out!

"""

verb_dict = {
  "say": say,
  "examine": examine,
}

"""

Combine this code with the one in our previous example, and run the program.

"""

>>>
: say Hello!
You said "Hello!"

: examine goblin
goblin
A foul creature

: examine elf
There is no elf here.
:
 
 """
 
 Combine this code with the one in our previous example, and run the program.
 
 """

 

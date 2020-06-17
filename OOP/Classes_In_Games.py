"""

 Object-orientation is very useful when managing different objects and their relations.
 That is especially useful when you are developing games with different characters and features.
 
 Let's look at an example project that shows how classes are used in game development.
 The game to be developed is an old fashioned text-based adventure game.
 Below is the function handling input and simple parsing.
 
"""

#1

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

#2

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self
       
    def get_desc(self):
        return self.class_name + "\n" + self.desc

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
 
 """
 
 This code adds more detail to the Goblin class and allows you to fight goblins.
 
 """
 
 #3
 
 class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = " A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >=3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

def hit(noun):
      if noun in GameObject.objects:
            thing = GameObject.objects[noun]
            if type(thing) == Goblin:
                  thing.health = thing.health - 1
                  if thing.health <= 0:
                        msg = "You killed the goblin!"
                  else:
                        msg = "You hit the {}".format(thing.class_name)
      else:
            msg ="There is no {} here.".format(noun)
      return msg
     
"""
>>>
: hit goblin
You hit the goblin

: examine goblin
goblin
 A foul creature
It has a wound on its knee.

: hit goblin
You hit the goblin

: hit goblin
You killed the goblin!

: examine goblin
A goblin

goblin
 A foul creature
It is dead.
:
"""
 
This was just a simple sample.
You could create different classes (e.g., elves, orcs, humans), fight them, make them fight each other, and so on.

"""



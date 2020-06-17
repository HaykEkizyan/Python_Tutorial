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



 

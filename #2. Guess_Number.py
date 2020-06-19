#1 It's a simple example of creating guess game with concret number(9 in this example).

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')

    
    
#2 It's an example with random number

import random

print("Number guessing game")

# randint function to generate the random number between 1 to 9
number = random.randint(0, 9)


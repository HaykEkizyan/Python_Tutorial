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
number = random.randint(0, 9)                # "randint" function to generate the random number between 1 to 9

chances = 0                                  # Number of chances to be given to the user to guess the number or it is the 
                                             # inputs given by user into input box here naumber of chances are 3
print("Guess a number (between 0 and 9): ")

while loop to count the number of chances
while chances < 3:
    guess = int(input())                     # Enter a number between 0 yo 9
    if guess == number:                      # Compare the user entered number with the number to be guessed
        print("Congratulation YOU WON!!!")   # If number entered by user is same as the generated number by randint
                                             # function then break from loop using loop control statement "break"

    elif guess < number:                     # Check if the user entered number is smaller than the generated number
        print("Your guess was too low: Guess a number higher than", guess)
    
     else:                                   # The user entered number is greater than the generated number
        print("Your guess was too high: Guess a number lower than", guess)
            
     chances += 1                            # Increase the value of chance by 1  
 
if not chances < 3:                          # Check whether the user guessed the correct number  
    print("YOU LOSE!!! The number is", number)

    
    

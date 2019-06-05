# Modules
import random

print("Rock, Paper, Scissors, Shoot!")

# Capture Input

user_choice = input('Please Select ROCK, PAPER, or SCISSORS: ')
print('-------------')
print("YOU CHOSE: ",user_choice)

# Validating  Inputs

options = ['rock','paper','scissors']

if user_choice.lower() not in options:
    print("That's an invalid choice. Try again.")
    exit()

# Generate Computer Selection

computer_choice = random.choice(options).capitalize()
print("COMPUTER CHOSE :",computer_choice)

# Determine Winner










# Display Final Outcomes







### NO LONGER USED
# if user_choice.lower() in options:
#     pass
# else:
#     print("That's an invalid choice. Try again.")
#     exit()

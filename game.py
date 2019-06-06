# Modules
import random

print("Rock, Paper, Scissors, Shoot!")

# Capture Input

user_choice = input('Please Select ROCK, PAPER, or SCISSORS: ')
smalluser_choice = user_choice.lower()
print('------------------')
print("YOU CHOSE: ",user_choice)

# Validating  Inputs

options = ['rock','paper','scissors']

if user_choice.lower() not in options:
    print("That's an invalid choice. Try again.")
    exit()

# Generate Computer Selection

computer_choice = random.choice(options)

print("------------------")
print("...GENERATING...")
print("COMPUTER CHOSE:",computer_choice.capitalize())

# Determine Winner and Display Final Outcomes
print("------------------")
print("...GENERATING...")

if smalluser_choice == computer_choice:
    print("TIE!")
elif smalluser_choice == "rock" and computer_choice == "paper":
    print("Computer wins!")
elif smalluser_choice == "rock" and computer_choice == "scissors":
    print("You win!")    
elif smalluser_choice == "paper" and computer_choice == "rock":
    print("Computer wins!")
elif smalluser_choice == "paper" and computer_choice == "scissors":
    print("Computer wins!")   
elif smalluser_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif smalluser_choice == "scissors" and computer_choice == "rock":
    print("Computer wins!")   
elif smalluser_choice == "rock" and computer_choice == "paper":
    print("Computer wins!")
elif smalluser_choice == "paper" and computer_choice == "scissors":
    print("Computer wins!")  



# winners = {
#     "rock":{
#         "rock":None,
#         "paper":"Paper",
#         "scissors":"Rock"
#     },
#     "paper":{
#         "paper":None,
#         "rock":"Paper",
#         "scissors":"Scissors"
#     },
#     "scissors":{
#         "scissors":None,
#         "rock":"Rock",
#         "paper":"Scissors"
#     },
# }

# winning_choice = winners[user_choice][computer_choice]

# if winning_choice:
#     if winning_choice == user_choice:
#         print ("YOU WON")
#     elif winning_choice == computer_choice:
#         print ("YOU LOSE!")

# R > S
# P > R
# S > P
# SAME = TIE

### NO LONGER USED
# if user_choice.lower() in options:
#     pass
# else:
#     print("That's an invalid choice. Try again.")
#     exit()

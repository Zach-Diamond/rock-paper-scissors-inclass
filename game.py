print("Rock, Paper, Scissors, Shoot!")

# Capture Input

user_choice = input('Please Select ROCK, PAPER, or SCISSORS: ')
print('-------------')
print("YOU CHOSE: ",user_choice)


# Validating  Inputs

options = ['rock','paper','scissors']

if user_choice.lower() in options:
    user_choice
else:
    print("That's an invalid choice. Try again.")
    exit()

# Generate Computer Selection

print("Generating...")

# Determine Winner

# Display Final Outcomes
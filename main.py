                                                       #PROJECT 1: SNAKE, WATER, GUN GAME 
# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.

'''
1 for rock
-1 for paper
0 for sesssior
'''


import random

# Mapping user input to choices
choices = {'R': 1, 'P': -1, 'S': 0}

# Get user's choice
user_choice = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()

# Convert user choice to number
user_choice_num = choices[user_choice]

# Generate computer's choice randomly
computer_choice_num = random.choice([0, -1, 1])

# Determine the choices in words for display
choices_words = {1: 'Rock', -1: 'Paper', 0: 'Scissors'}

# Print choices
print(f"You chose {choices_words[user_choice_num]}")
print(f"Computer chose {choices_words[computer_choice_num]}")

# Determine the winner
if user_choice_num == computer_choice_num:
    print("It's a draw!")
elif (user_choice_num == 1 and computer_choice_num == 0) or (user_choice_num == -1 and computer_choice_num == 1) or (user_choice_num == 0 and computer_choice_num == -1):
    print("You win!")
else:
    print("Computer wins!")

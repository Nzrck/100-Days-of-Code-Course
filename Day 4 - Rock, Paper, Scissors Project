rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Take the user input, and generate a random input for computer, make sure data type matches, collate the results
# Collate the graphics variables into a list, input number can be used as index to select the graphic to display
import random

rps_graphics = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_input = random.randint(0, 2)
combined_input = [user_input, computer_input]

# Establish the rules for wining that can be compared to the combined inputs
win_condition = [[0, 2], [1, 0], [2, 1]]
# Create the visual output and results output logic
if user_input == 0 or user_input == 1 or user_input == 2:
    print(rps_graphics[user_input])
    print(f"Computer chose:\n {rps_graphics[computer_input]}")
    if user_input == computer_input:
        print("It's a draw")
    elif combined_input in win_condition:
        print("You win!")
    else:
        print("You lose")
else:
    print("You typed an invalid number, you lose!")

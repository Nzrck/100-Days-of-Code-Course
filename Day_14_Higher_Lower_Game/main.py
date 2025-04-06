# TODO #0: Import required modules / functions / variables (random, game_data, art)
import random
import art
from game_data import data

# TODO #3: Create constants for game messages.
RULES_MSG= "Welcome! In this game you are presented with two famous instagram accounts.\nYour aim is to guess which account has more followers.\nThe game will continue until you guess incorrectly."
COMPARE_MSG = "Compare A: {}, a {}, from {}."
AGAINST_MSG = "Against B: {}, a {}, from {}."
CHOICE_MSG = "Who has more followers? Type 'A' or 'B': "
CORRECT_MSG = "You are right! Current score: {}."
ROUND_MSG = "Would you like to play another round? Type 'Y' or 'N':  "
INCORRECT_MSG = "Sorry, that was an incorrect guess. Your final score: {}"
VALIDATION_MSG = "Sorry, your input was NOT valid. Please type {}"

def input_validation(user_input, stage):
    while True:
        if stage == "guess":
            if user_input == "a" or user_input == "b":
                return user_input
            else:
                user_input = input(VALIDATION_MSG.format("'A' or 'B': ")).lower()
        if stage == "another_round":
            if user_input == "y" or user_input == "n":
                return user_input
            else:
                user_input = input(VALIDATION_MSG.format("'Y' or 'N': ")).lower()

def compare_followers(follower_data):
    if follower_data[0]['follower_count'] > follower_data[1]['follower_count']:
        return "a"
    else:
        return "b"

# TODO #1: Create a function to encompass the game and re-run the function if user wants to play another round
def higher_lower():
    # TODO #2: Create a variable to track player score. Use the variable to initate and loop the game progress.
    player_score = 0
    # TODO #4: Create a loop for game progress.
    # TODO  #4.1: Select two random entries from data, ensure duplicates not selected.
    # TODO  #4.2: Compare follower values of the two random entries selected. Return key for higher value.
    # TODO  #4.3: Display messages to the user, take user input for the guess.
    game_data = random.sample(data, 2)
    while player_score > -1:
        winning_answer = compare_followers(game_data)
        print(art.logo)

        if player_score == 0:
            print(RULES_MSG)
            print(COMPARE_MSG.format(game_data[0]['name'],game_data[0]['description'],game_data[0]['country']))
        else:
            print(CORRECT_MSG.format(player_score))
            print(COMPARE_MSG.format(game_data[0]['name'],game_data[0]['description'],game_data[0]['country']))

        print(art.vs)
        print(AGAINST_MSG.format(game_data[1]['name'],game_data[1]['description'],game_data[1]['country']))

        # TODO  #5: Validate the user input, if input is not valid request re-input until valid. If input is valid, return the input back to game function.
        user_choice = input_validation(input(CHOICE_MSG).lower(), "guess")

        # TODO #6: Check if user input input is correct.
        # TODO  #6.1: If user input is correct, increase player score, provide feedback to user. Clear terminal and return to TODO #5.
        # TODO  #6.2: If user input is incorrect, feedback to the player and display final score. Ask user if they want to player another round. Validate input.
        # TODO      #6.2.1: If user wants another round, continue the game_loop and clear player score variable.
        # TODO      #6.2.2: If user does not want another round, break the game_loop.
        if user_choice == winning_answer:
            player_score += 1
            game_data = [game_data[1]]
            rebuild_game_data = True
            while rebuild_game_data:
                new_entry = random.choice(data)
                if new_entry in game_data:
                    new_entry = random.choice(data)
                else:
                    game_data.append(new_entry)
                    rebuild_game_data = False
                    print("\n" * 20)
        else:
            print(INCORRECT_MSG.format(player_score))
            another_round = input_validation(input(ROUND_MSG).lower(), "another_round")
            if another_round == "y":
                print("\n" * 20)
                return True
            else:
                return False

game_loop = True

while game_loop:
    game_loop = higher_lower()

# TODO #1: Import random module for number generation and the logo from art module
from art import logo
import random

# Refactored code, created STR_DICT global dictionary to store strings prompts for the game.
STR_DICT = {
    'welcome_msg': "{}\nWelcome to Guess The Number!\n",
    'game_objective': "In this game, we have selected a random number between 1 and 100. Your goal is to guess the number.",
    'game_difficulty_rules': "There are two difficulty modes: 'easy' or 'hard'.\nYou get 10 guess attempts (easy) or 5 guess attempts (hard).",
    'difficulty_input': "\nChoose your difficulty. Type 'easy' or 'hard': ",
    'attempt_counter': "Your remaining attempts: [{}]\n",
    'player_guess': "Make a guess: ",
    'guess_high': "Your guess was too high.\nTry again.",
    'guess_low': "Your guess was too low.\nTry again.",
    'game_win': "Congratulations your guess was correct ({})!\n Would you like to start another game?\n Type 'yes' or 'no': ",
    'game_loss': "Your final guess was incorrect. The correct number was: {}\n Would you like to start another game?\n Type 'yes' or 'no': ",
    'difficulty_validation': "\nYour difficulty section was not valid! Please select again: ",
    'guess_validation': "Your guess was not a valid number! Your remaining attempts have not been changed.\nEnter a valid number.",
    'conclude_validation': " Your selection was invalid! To continue the game type 'yes' or to exit type 'no': ",
}

def input_validation(user_input, validation_stage):
    """Takes and validates all user inputs into the game (difficulty selection, guesses, game restart).
    Returns input once valid."""

    while True:
        if validation_stage == "difficulty":
            if user_input == "easy" or user_input == "hard":
                return user_input
            else:
                user_input = input(STR_DICT['difficulty_validation']).lower()

        elif validation_stage == "guess_attempts":
            if not user_input.isnumeric():
                print(STR_DICT['guess_validation'])
                user_input = input(STR_DICT['player_guess'])
            else:
                return user_input

        elif validation_stage == "conclude_game":
            if user_input == "yes" or user_input == "no":
                return user_input
            else:
                user_input = input(STR_DICT['conclude_validation']).lower()

def difficulty_selection():
    """Takes user input to select difficulty.
    Returns value(int) of guess attempts user can make."""

    difficulty = input_validation(input(STR_DICT['difficulty_input']).lower(), "difficulty")

    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

def conclude_game(outcome, target):
    """Takes game outcome and target number.
    Displays outcome to user.
    Takes user input to start another game or continue.
    Returns True / False to global game_on loop."""

    if outcome == "win":
        choice = input(STR_DICT['game_win'].format(target)).lower()
    else:
        choice = input(STR_DICT['game_loss'].format(target)).lower()

    restart_choice = input_validation(choice, "conclude_game")

    if restart_choice == "yes":
        print("\n" * 20)
        return True
    elif restart_choice == "no":
        return False

# TODO #2: Create the main function to encompass the game. Print the logo and a welcome message.
#  Generate a random number between 1 - 100.

def number_guessing_game():
    print(STR_DICT['welcome_msg'].format(logo))
    number_to_guess = random.randint(1, 100)

    # TODO #3: Explain the game rules and take user input for difficulty.
    #  Create a variable for number of guess attempts, update based on difficulty selection and validate user input.

    print(STR_DICT['game_objective'])
    print(STR_DICT['game_difficulty_rules'])
    guess_attempts = difficulty_selection()


    # TODO #4: Create a while loop dependant on remaining user guesses attempts. Display attempts left. Take user guess and validate the input.
    #  If correct: Conclude the game, take input for restarting the game and validate.
    #  If NOT correct: Subtract an attempt from guesses variable.
    #  If user does not not have guess attempts left: Conclude the game, display the correct number. Take input for restarting the game and validate.
    #  If user has guess attempts left : Feedback to user if their guess is greater or lower than the number.

    while guess_attempts > 0:
        print(STR_DICT['attempt_counter'].format(guess_attempts))
        guess = input_validation(input(STR_DICT['player_guess']), "guess_attempts")
        if int(guess) == number_to_guess:
            conclusion = conclude_game("win", number_to_guess)
            return conclusion
        else:
            guess_attempts -= 1
            if guess_attempts == 0:
               conclusion = conclude_game("loss", number_to_guess)
               return conclusion
            elif int(guess) > number_to_guess:
                print(STR_DICT['guess_high'])
            else:
                print(STR_DICT['guess_low'])


# TODO #5 : Call the game function to start the program. Loop the function based on user input.

game_on = True
while game_on:
    game_on = number_guessing_game()

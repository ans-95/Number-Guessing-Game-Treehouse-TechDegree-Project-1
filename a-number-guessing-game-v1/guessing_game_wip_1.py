"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import statistics 
import random   
# Create the start_game function.
def start_game(): 
    # Write your code inside this function.

    #   When the program starts, we want to:
    #   ------------------------------------
    #   1. Display an intro/welcome message to the player.
    print("Welcome player to the number guessing game! ")
    #   2. Store a random number as the answer/solution.
    answer = randint(1, 10)
    #   3. Continuously prompt the player for a guess.
    guess = int(input("Guess a number from 1 - 10: "))
    attempts = 1
    attempts_list = []
    all_attempts = []
    while guess != answer: 
    #     a. If the guess is greater than the solution, display to the player "It's lower".
        if guess < answer:
            print("It's lower. Try again.")
            attempts += 1
            #     b. If the guess is less than the solution, display to the player "It's higher".
        elif guess > answer:
            print("It's higher. Try again.")
            attempts += 1
        # elif guess < 0 or guess > 10:
            # print("Please enter a number between 1 and 10. Try again.")
        # elif guess != int(guess):
           # print("Input invalid. Please enter a number between 1 and 10. Try again.")
            #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
        else:
            print("Got it!")
            print(attempts)
            print(attempts_list)
            attempts_list.append(attempts)
            break
    #   5. Display the following data to the player
    #     a. How many attempts it took them to get the correct number in this game
    print("It took you {} attempts to guess the correct number in this game.".format(attempts))
    #   Overall Statistics
    print("Overall Statistics:")
    #     b. The mean of the saved attempts list
    average = mean(attempts_list)
    print("Mean: {}".format(mean))
    #     c. The median of the saved attempts list
    median_attempts = median(attempts_list)
    print("Median: {}".format(median))
    #     d. The mode of the saved attempts list
    mode_attempts = mode(attempts_list)
    print("Mode: {}".format(mode))
    #   6. Prompt the player to play again
    play_again = input("Would you like to play again? Enter y/n ")
    #     a. If they decide to play again, start the game loop over.
    
    if play_again.lower() == "y":
        print("Let's start again")
        start_game
    #     b. If they decide to quit, show them a goodbye message.
    else:
        # play_again.lower() == "n"
        all_attempts.append(guesses_list)
        print("Thanks for playing! Good bye!")
# ( You can add more features/enhancements if you'd like to. )
#high_score = min(all_attempts)

# Kick off the program by calling the start_game function.
start_game()

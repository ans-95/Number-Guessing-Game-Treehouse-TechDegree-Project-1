"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import statistics 
import random
# Create an empty list of all attempts ever done for high score
# def all_attempts_list():
  # global all_attempts
  # all_atttempts = []

# all_attempts_list()
# Let's see if putting empty attempts list here makes a difference
def attempts_list():
  global attempts_list
  attempts_list = []

attempts_list()

# Create the start_game function.
def start_game(): 
    # Write your code inside this function.
    guess = None
    attempts = 0
    # high_score = None 
    #   When the program starts, we want to:
    #   ------------------------------------
    #   1. Display an intro/welcome message to the player.
    print("Welcome player to the number guessing game! ")
    #   2. Store a random number as the answer/solution.
    answer = random.randint(1, 10)
    #   2.5. High-score message to the player.
    # print(f"Can you beat the current high score of {high_score}?")

    #   3. Continuously prompt the player for a guess.
    while guess != answer:
        try:
            guess = int(input("Guess a number from 1 - 10: "))
            # print(answer)
    #     a. If the guess is greater than the solution, display to the player "It's lower".
            if guess < 0 or guess > 10:
                print("Please enter a number from 1 and 10. Try again.")
                #     b. If the guess is less than the solution, display to the player "It's higher".
            elif guess > answer:
                print("It's lower. Try again.")
                attempts += 1
            elif guess < answer:
                print("It's higher. Try again.")
                attempts += 1
                #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
            else:
                print("Got it!")
                attempts += 1
                attempts_list.append(attempts)
                # all_attempts_list.append(attempts_list)
                # print(attempts)
                # print(attempts_list)
                # print(all_attempts_list)
                #   5. Display the following data to the player
                #     a. How many attempts it took them to get the correct number in this game
                print("It took you {} attempts to guess the correct number in this game.".format(attempts))
                #   Overall Statistics
                print("Overall Statistics:")
                #     b. The mean of the saved attempts list
                average = statistics.mean(attempts_list)
                print(f"Mean: {average}")
                #     c. The median of the saved attempts list
                median_attempts = statistics.median(attempts_list)
                print(f"Median: {median_attempts}")
                #     d. The mode of the saved attempts list
                mode_attempts = statistics.mode(attempts_list)
                print(f"Mode: {mode_attempts}")
    #   6. Prompt the player to play again
                play_again = input("Would you like to play again? Enter y/n: ")
        #     a. If they decide to play again, start the game loop over.
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    print("Let's start again!")
                    start_game()
        #     b. If they decide to quit, show them a goodbye message.
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    print("Thanks for playing! Good bye!")
                    break                
                else:
                    print("Invalid input. Exiting the game.")
                    break
        except ValueError:
            print("Please enter a valid integer between 1 to 10.")
        
        
                    
# ( You can add more features/enhancements if you'd like to. )
#   high score
# def high_score():
    # global high_score
    # high_score = min(attempts_list)
    
# high_score()

# Kick off the program by calling the start_game function.
start_game()

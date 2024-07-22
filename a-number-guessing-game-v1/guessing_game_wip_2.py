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
    answer = random.randint(1, 10)
    #   3. Continuously prompt the player for a guess.
    attempts_list = []
    all_attempts = []
    guess = 0
    attempts = 0
    while guess != answer:
        try:
            guess = int(input("Guess a number from 1 - 10: "))
            attempts += 1
            # print(answer)
    #     a. If the guess is greater than the solution, display to the player "It's lower".
            if guess < answer:
                print("It's higher. Try again.")
                #     b. If the guess is less than the solution, display to the player "It's higher".
            elif guess > answer:
                print("It's lower. Try again.")
            # elif guess < 0 or guess > 10:
                # print("Please enter a number between 1 and 10. Try again.")
            # elif guess != int(guess):
               # print("Input invalid. Please enter a number between 1 and 10. Try again.")
                #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
            else:
                print("Got it!")
                # print(attempts)
                # print(attempts_list)
                attempts_list.append(attempts)
                #   5. Display the following data to the player
                #     a. How many attempts it took them to get the correct number in this game
                print("It took you {} attempts to guess the correct number in this game.".format(attempts))
                #   Overall Statistics
                print("Overall Statistics:")
                #     b. The mean of the saved attempts list
                average = statistics.mean(attempts_list)
                print("Mean: {}".format(average))
                #     c. The median of the saved attempts list
                median_attempts = statistics.median(attempts_list)
                print("Median: {}".format(median_attempts))
                #     d. The mode of the saved attempts list
                mode_attempts = statistics.mode(attempts_list)
                print("Mode: {}".format(mode_attempts))
                #   6. Prompt the player to play again
                play_again = input("Would you like to play again? Enter y/n ")
            #     a. If they decide to play again, start the game loop over.
            while True:
                start_game()
                if play_again.lower() == "y" or "yes":
                    print("Let's start again")
                    continue
                elif play_again.lower() == "n" or "no":
                    all_attempts.append(guesses_list)
                    print("Thanks for playing! Good bye!")
                    break                
                #     b. If they decide to quit, show them a goodbye message.
                else:
                    print("Invalid input. Exiting the game.")
                    break
        except ValueError:
            print("Please enter a valid integer between 1 to 10.")
                    
# ( You can add more features/enhancements if you'd like to. )
#high_score = min(all_attempts)

# Kick off the program by calling the start_game function.
start_game()

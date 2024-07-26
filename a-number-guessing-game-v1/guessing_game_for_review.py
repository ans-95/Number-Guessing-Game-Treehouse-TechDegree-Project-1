"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
# In addition to coding the functionality of this guessing game program, I also formatted the string for easier readablity when users play the game.
# Import the random and statistics modules.
import statistics 
import random

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
    high_score = None 
    #   When the program starts, we want to:
    #   ------------------------------------
    #   1. Display an intro/welcome message to the player.
    print("=================================================\n Welcome player to the number guessing game! \n=================================================")
    #   2. Store a random number as the answer/solution.
    answer = random.randint(1, 10)

    #   3. While loop to prompt the user to guess the correct answer continously until the user guesses correctly.
    while guess != answer:
        try:
          # a if statement to define the high_score variable in relation to the attempts_list variable
            if attempts_list:
              high_score = min(attempts_list)
              print(f"Can you beat the current high score of {high_score}? ")
            guess = int(input("___________________________\nGuess a number from 1 - 10: "))
    #     a. If the guess is greater than the solution, display to the player "It's lower".
            if guess < 0 or guess > 10:
                print("Please enter a number from 1 and 10. Try again.\n_____________________________________")
                #     b. If the guess is less than the solution, display to the player "It's higher".
            elif guess > answer:
                print("It's lower. Try again. \n___________________________")
                attempts += 1
            elif guess < answer:
                print("It's higher. Try again. \n___________________________")
                attempts += 1
                #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
            else:
                print("Got it!")
                attempts += 1
                attempts_list.append(attempts)
                #   5. Display the following data to the player
                #     a. How many attempts it took them to get the correct number in this game
                print("It took you {} attempts to guess the correct number in this game.".format(attempts))
                #   Overall Statistics
                print("\n____________________\nOverall Statistics:\n____________________")
                #     b. The mean of the saved attempts list
                average = statistics.mean(attempts_list)
                print(f"Mean: {average}")
                #     c. The median of the saved attempts list
                median_attempts = statistics.median(attempts_list)
                print(f"Median: {median_attempts}")
                #     d. The mode of the saved attempts list
                mode_attempts = statistics.mode(attempts_list)
                print(f"Mode: {mode_attempts}")
                # A series of statements to print out depending of if the user beat the high score or not
                if high_score == None:
                  print(f"__________________________________\nYou set a high score of {attempts} attempts!\n__________________________________")
                elif attempts < high_score:
                  print(f"___________________________________________\nYou've set a new high score of {attempts} attempts!n\___________________________________________")
                elif attempts == high_score:
                  print("_____________________________________________________________________\nYour number of attempts is tied with the current high score.\n Please play again to try to beat the high score!\n_____________________________________________________________________")
                else:
                  print(f"__________________________________________________\nPlease try again to beat the current high score of {high_score}.\n__________________________________________________")
                        
    #   6. Prompt the player to play again
                play_again = input("________________________________________\nWould you like to play again? Enter y/n: ")
        #     a. If they decide to play again, start the game loop over.
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    print("\n-----------------\nLet's start again!\n-----------------")
                    start_game()
        #     b. If they decide to quit, show them a goodbye message.
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    print("Thanks for playing! Good bye!")
                    break                
                else:
                    print("Invalid input. Exiting the game.")
                    break
        # except line to print a statement for ValueErrors.
        except ValueError:
            print("Please enter a valid integer between 1 to 10.")
        
        
                    
# Kick off the program by calling the start_game function.
start_game()

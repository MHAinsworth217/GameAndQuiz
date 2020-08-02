# Matthew Ainsworth
# Rock Paper Scissors
# 26/07/2020

# Import relevant modules
import random
import time
import sys


# Define the game function
def game():
    # Set up game to run unless user exits
    while True:
        # Randomise computer choice
        number = random.randint(1, 3)
        print("Please pick either Rock, Paper or Scissors! Or enter Exit to exit the program:")
        # Take in user choice
        usrchoice = input()
        time.sleep(1)
        # Correlate user's choice to a number
        if usrchoice.casefold() == "rock":
            usrnum = 1
        elif usrchoice.casefold() == "paper":
            usrnum = 2
        elif usrchoice.casefold() == "scissors":
            usrnum = 3
        # Exit if user wishes
        elif usrchoice.casefold() == "exit":
            print("Goodbye")
            break
        # Ensure user enters a valid choice
        else:
            print("Please enter a valid choice.")

        # The following block code decides the game's outcome based on the user's and computer's number
        # Same choice (tie)
        if usrnum == number:
            print("It's a tie! Please try again.")
            time.sleep(1)
        # Rock vs Paper (CPU wins)
        elif usrnum == 1 and number == 2:
            print("I choose paper! I win!")
            time.sleep(1)
        # Rock vs Scissors (User wins)
        elif usrnum == 1 and number == 3:
            print("I choose scissors! You win!")
            time.sleep(1)
        # Paper vs Rock (User wins)
        elif usrnum == 2 and number == 1:
            print("I choose rock! You win!")
            time.sleep(1)
        # Paper vs Scissors (CPU wins)
        elif usrnum == 2 and number == 3:
            print("I choose scissors! I win!")
            time.sleep(1)
        # Scissors vs Rock (CPU wins)
        elif usrnum == 3 and number == 1:
            print("I choose rock! I win!")
            time.sleep(1)
        # Scissors vs Paper (User wins)
        elif usrnum == 3 and number == 2:
            print("I choose paper! You win!")
            time.sleep(1)


# Define Quiz function
def quiz():
    # Set score to 0
    score = 0
    # Set the answers in a list
    answers = ["london",
               "oxygen",
               "basketball",
               "javascript",
               "kid cudi"]
    print("Welcome to the Quiz! Please answer the following 5 questions.")
    time.sleep(1)
    # The following block of code asks the questions, checks the answer and adds to the user's score accordingly
    print("What is the capital of England?")
    userans = input()
    if userans.casefold() == answers[0]:
        score += 1
    time.sleep(1)
    print("What does O stand for on the periodic table?")
    userans = input()
    if userans.casefold() == answers[1]:
        score += 1
    time.sleep(1)
    print("What sport did Kobe Bryant play?")
    userans = input()
    if userans.casefold() == answers[2]:
        score += 1
    time.sleep(1)
    print("What is the most popular programming language according to Business Insider?")
    userans = input()
    if userans.casefold() == answers[3]:
        score += 1
    time.sleep(1)
    print("Who released the album Man on the Moon: The End of Day in 2009?")
    userans = input()
    if userans.casefold() == answers[4]:
        score += 1
    time.sleep(1)
    # Print the user's score
    print("You scored {}/5".format(score))


# Start program, welcoming the user
print("Welcome! Please select either the game or the quiz. Or enter exit to exit:")
usersChoice = input()
if usersChoice.casefold() == "game":
    game()
elif usersChoice.casefold() == "quiz":
    quiz()
elif usersChoice.casefold() == "exit":
    sys.exit()
else:
    print("Please enter a valid choice:")
    time.sleep(1)

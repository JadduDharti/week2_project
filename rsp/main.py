# Rock-Paper-Scissors Application

# For this project, you and your partner(s) will work to create a program that has a
# "player" and a "computer" adversary.
# The computer should randomly choose its decision based on a
# list of actions it can take("Rock", "Paper" or "Scissors").
# The player should then have a chance to input their decision.


# Main Coding starts from here.

# importing file for random pic

import random

# Printing some multilines for game rules

print("Winning rules of the game ROCK PAPER SCISSORS are: ")
print("\n Rock vs Paper -->> Paper wins")
print("Rock vs Scissor -->> Rock wins")
print("Paper vs scissor -->> Scissor wins")
print("Rock vs Rock -->> Its a Tie")


# Going thru the loop to get user input

while True:
    choice = 0
    choice_name = ""

    print("1 for Rock")
    print("2 for Paper")
    print("3 for Scissor")

    # taking user input

    choice = int(input("Enter your Choice: "))

    # if anyone of the condition is true value
    # else return to user for invalud input

    while choice > 3 or choice < 1:
        choice = int(input("Enter the valid input (1 / 2 / 3): "))

    # initalizing the value of the choice variable

    if choice == 1:
        choice_name = "rock"
    elif choice == 2:
        choice_name = "paper"
    else:
        choice_name = "scissor"

    # printing user input
    print("User choice is: ", choice_name.title())

    print("Now its Computer Turn...")

    # Computer choode rndomly any number

    possible_actions = ["rock", "paper", "scissors"]
    comp_choice_name = random.choice(possible_actions)

    # comp_choice = random.randint(1, 3)

    # initialize the computer variable
    if comp_choice_name == "rock":
        comp_choice = 1
    elif comp_choice_name == "paper":
        comp_choice = 2
    else:
        comp_choice = 3

    print("Computer choice is: ", comp_choice_name.title())
    print(f"{choice_name.upper()} vs. {comp_choice_name.upper()}")

    # checking the conditions for draw or tie

    if choice == comp_choice:
        result = "TIE"

    # Checking condition for winner

    # if user pick is equal to rock and comp is equal to paper, result =
    if (choice == 1 and comp_choice == 2):
        result = "PAPER"
    elif (choice == 2 and comp_choice == 1):
        result = "PAPER"

    # if user pick is equal to rock and comp is equal to scissor, result =
    if (choice == 1 and comp_choice == 3):
        result = "ROCK"
    elif (choice == 3 and comp_choice == 1):
        result = "ROCK"

    # if user pick is equal to paper and comp is equat to scissor, result =
    if (choice == 2 and comp_choice == 3):
        result = "SCISSOR"
    elif (choice == 3 and comp_choice == 2):
        result = "SCISSOR"

    # Printing the result of the match
    if result == "TIE":
        print("<<------ ITS A TIE ------>>")
    elif result == choice_name.upper():
        print("<<------ YOU ARE WINNER ------>>")
    else:
        print("<<------ COMPUTER IS A WINNER ------>>")

    # asking user if they want to continue or not

    ans = input("Do you want to play again? (yes / no): ").lower()

    while ans not in ("yes", "no"):
        ans = input("Do you want to play again? (yes / no): ").lower()
    if ans == "no":
        print("Nice to play with you")
        break

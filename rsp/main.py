# Rock-Paper-Scissors Application

#For this project, you and your partner(s) will work to create a program that has a 
#"player" and a "computer" adversary. 
#The computer should randomly choose its decision based on a 
#list of actions it can take("Rock", "Paper" or "Scissors"). 
#The player should then have a chance to input their decision.



#Main Coding starts from here.

#importing file for random pic

import random

#Printing some multilines for game rules

print("Winning rules of the game ROCK PAPER SCISSORS are: ")
print("\n Rock vs Paper -->> Paper wins")
print("Rock vs Scissor -->> Rock wins")
print("Paper vs scissor -->> Scissor wins")
print("Rock vs Rock -->> Its a Tie")


#Going thru the loop to get user input

while True:
    print("1 for Rock")
    print("2 for Paper")
    print("3 for Scissor")
    
    #taking user input
    
    choice = int(input("Enter your Choice: "))

    # if anyone of the condition is true value 
    # else return to user for invalud input

    while choice > 4 or choice < 1:
        choice = int(input("Enter the valid input (1 / 2 / 3): "))

    
    #initalizing the value of the choice variable

    if choice == 1:
        choice_name = "rock"
    elif choice == 2:
        choice_name = "paper"
    else:
        choice_name == "scissor"
   
    #printing user input
    print("User choice is: ", choice_name.title())

    print("Now its Computer Turn...")

    #Computer choode rndomly any number
    comp_choice = random.randint(1,3)

    #initialize the computer veriable
    
    if comp_choice == 1:
        comp_choice_name = "rock"
    elif comp_choice == 2:
        comp_choice_name = "paper"
    else:
        comp_choice_name == "scissor"
    
    print("Computer choice is: ", comp_choice_name.title())
    print(f"{choice_name} vs. {comp_choice_name}")

    #checking the conditions for draw or tie

    if choice == comp_choice:
        result = "TIE"

    #Checking condition for winner









    # Printing the result of the match
    if result == "TIE":
        print("<<------ ITS A TIE ------>>")
    elif result == choice_name.upper():
        print("<<------ YOU ARE WINNER ------>>")
    else:
        print("<<------ COMPUTER IS A WINNER ------>>")

    
    #asking user if they want to continue or not

    ans = input("Do you want to play again? (yes / no): ").lower()

    if ans == "n":
        print("Nice to play with you")
        break;




    



      

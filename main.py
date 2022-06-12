from multiprocessing import RLock, parent_process
from typing import ParamSpecArgs
import random
""" how to play game"""
#rock smashes scissors
#paper covers Rock 
#scissors cuts paper

print("\033c")
#players
options= ["R", "P", "S"]

# take input from user 
print("How to play  the game.\n \n Rock smashes scissors. \n Paper covers Rock.\n Scissors cuts paper. \n")
print("The play options are: R = Rock", "P = Paper", "S = Scissors \n")
while True:
    choice = input("Pick a Player \n R, P, S:  ")

#check if choice is one of the three options 
    choice == ["R", "P", "S"]
  
    while choice not in ["R", "P", "S"]:
        choice = input ("please pick a player again\n R = rock, P = paper, S = scissors:  ")

#time for computer to select
    computer_choice = random.choice(options)
    print (f"\n you picked {choice} and computer picked {computer_choice}. \n")

#time to play
    if choice == computer_choice:
        print(f"it's a tie! players selected {choice} ")

    elif choice == "R":
        if computer_choice == "S":
            print("Hooray! rock has smashed scissors! Congratulations you win!!!")
        else:
            print("Oops....unfortunately, paper covers rock. You lost to computer")

    elif choice == "P":
        if computer_choice == "R":
            print("Hooray! paper covers rock! Congratulations you win!!!")
        else:
            print("Oops....unfortunately, scissors cuts paper. You lost to computer")

    elif  choice == "S":
        if computer_choice == "P":
            print("Hooray! scissors cuts paper! Congratulations you win!!!")
        else:
            print("Oops....unfortunately, scissors cuts paper. You lost to computer")

# play another game
    another_game = input("Do you want to play another game? (yes/no): ")
    if another_game != "yes":
        print("Goodbye")
        break

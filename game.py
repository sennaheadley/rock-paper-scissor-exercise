# this is the "game.py" file...
import random
import os

from dotenv import load_dotenv
load_dotenv()

playername = os.getenv("PLAYER_NAME")

print("Welcome", playername, "to my Rock-Paper-Scissors game...")
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
if user_choice in ['rock','paper','scissors']:
    print("You chose:", user_choice) 
else: 
    print("Your choice is not valid.  Reminder: all letters should be lowercase!")
    print("Try again.")
    exit()
#Thank you to Dominic Parente for sharing his code chunk. 

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:", computer_choice)


if user_choice == "rock" and computer_choice == "scissors":
    print("You won this round!")
elif user_choice == "rock" and computer_choice == "paper":
    print("You lost this round!")
elif user_choice == "rock" and computer_choice == "rock":
    print("You tied this round!")
if user_choice == "paper" and computer_choice == "rock":
    print("You won this round!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You lost this round!")
elif user_choice == "paper" and computer_choice == "paper":
    print("You tied this round!")
if user_choice == "scissors" and computer_choice == "paper":
    print("You won this round!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You lost this round!")
elif user_choice == "scissors" and computer_choice == "scissors":
    print("You tied this round!")

print("Thanks for playing.")


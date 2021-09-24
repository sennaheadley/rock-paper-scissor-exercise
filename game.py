# this is the "game.py" file...
import random
import os

x = os.getenv("PLAYER_NAME")
print(x)


print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
print(user_choice)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print(computer_choice)

#breakpoint()

if user_choice == "rock" and computer_choice == "scissors":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You won this round!")
elif user_choice == "rock" and computer_choice == "paper":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You lost this round!")
elif user_choice == "rock" and computer_choice == "rock":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You tied this round!")
if user_choice == "paper" and computer_choice == "rock":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You won this round!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You lost this round!")
elif user_choice == "paper" and computer_choice == "paper":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You tied this round!")
if user_choice == "scissors" and computer_choice == "paper":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You won this round!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You lost this round!")
elif user_choice == "scissors" and computer_choice == "scissors":
    print("You chose",user_choice)
    print("The computer chose", computer_choice)
    print("You tied this round!")

print("Thanks for playing.")


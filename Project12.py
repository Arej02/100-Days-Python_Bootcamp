import random
from random import choice

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
number=random.randint(1,100)
print("I am thinking of a number between 1 and 100")

def set_difficulty():
    while True:
        choice=input("Choose the difficulty.(Hard or Easy):")
        if choice=="Easy":
            return EASY_LEVEL_TURNS
        elif choice=="Hard":
            return HARD_LEVEL_TURNS
        else:
            print("Please choose a valid option.")

def play_game(attempt):
    while attempt>0:
        user_guess=int(input("Enter a number:"))
        if(user_guess==number):
            print(f"You win.The number is {number}")
            return
        else:
            attempt-=1
            if attempt>0:
                print(f"You have {attempt} left")
                if number>user_guess:
                    print("The number is higher.Guess again")
                else:
                    print("The number is lower.Guess again")
            else:
                print(f"You are out of turns.The correct answer is {number}")

attempt=set_difficulty()
play_game(attempt)



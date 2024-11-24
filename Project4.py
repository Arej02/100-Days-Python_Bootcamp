# Rock
import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gameImage={"rock":rock,"paper":paper,"scissor":scissor}
user=input("What do you want to choose?(Rock,Paper,Scissor)").lower()


option=["rock","paper","scissor"]
if user not in option:
    print("Invalid choice!Please select Rock,Paper,Scissor")
else:
    computer = random.choice(option)

    print("\nYou choose:")
    print(gameImage[user])
    print("Computer chose:")
    print(gameImage[computer])
    if user=="rock" and computer=="scissor" or user=="scissor" and computer=="paper" or user=="paper" and computer=="rock":
        print("You win!")
    elif user==computer:
        print("It's a draw!")
    else:
        print("Computer wins!")


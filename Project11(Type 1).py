import random
from random import choice

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
computer=[]
player=[]

#Task 1:Randomly put 2 cards in computer and player and find their sum


player.append(random.choice(cards))
player.append(random.choice(cards))
sum1=sum(player)

print("Players cards:",player)
print("Player's sum:",sum1)

sum2=0
computer.append(random.choice(cards))
computer.append(random.choice(cards))
sum2=sum(computer)

print("Computer's cards:",computer)
print("Computer's sum:",sum2)

#Ask the user if they want to continue playing:
should_continue=True
while should_continue:
    choice=input("Do you want to continue playing?(y/n)")
    if choice=="y":
        player.append(random.choice(cards))
        sum1=sum(player)
        print("Players cards:", player)
        print("Player's sum:", sum1)
        if sum1>21:
            print(f"You lose.Computer Wins since your sum is {sum1}")
            should_continue=False
    elif choice=="n":
        should_continue=False
        print(f"Final Player's sum:{sum1}")
        print(f"Final Computer's sum:{sum2}")
        if sum1>21 or (sum2<=21 and sum2>=sum1):
            print("Computer Wins!")
        elif sum2>21 or (sum1<=21 and sum1>sum2):
            print("Player Wins!")
        else:
            print("It's a tie!")

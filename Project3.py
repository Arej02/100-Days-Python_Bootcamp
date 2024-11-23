#This is my project 3 ,for the treasure island
print('''         
            _ _~-___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D''')

print("Welcome to the Treasure Island!Your job is to find the treasure")
direction=input("Do you want to move left or right?(R/L)").upper()
if direction=="R":
    print("Game Over!")
elif direction=="L":
    level1=input("Do you want to swim or wait?(S/W)").upper()
    if level1=="S":
        print("Game Over!")
    elif level1=="W":
        level2=input("Which door do you want to choose?(Red/Blue/Yellow)").upper()
        if level2=="Red" and level2=="Blue":
            print("Game Over")
        elif level2=="Yellow":
            print("You Win!")
        else:
            print("Please choose the correct option!")
    else:
        print("Please choose the correct option!")


else:
    print("Please choose the correct option!")
import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        return "Draw"
    elif u_score==0:
        return "You win"
    elif c_score==0:
        return "You lose"
    elif u_score>21:
        return "You went over and you lose"
    elif c_score>21:
        return "You win"
    elif u_score>c_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards=[]
    computer_cards=[]
    user_score=-1
    computer_score=-1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over=False
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards are:{user_cards},and your current score is:{user_score}")
        print(f"The computer's card is:{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_choice=input("Do you want to add another card.(y/n)")
            if user_choice=="y":
                user_cards.append(deal_card())
                user_score=calculate_score(user_cards)
            if user_choice=="n":
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand is:{user_cards} and final score is:{user_score}")
    print(f"The computers hand is:{computer_cards} and final score is {computer_score}")

    print(compare(user_score,computer_score))

while input("Do you want to play another round?(y/n)")=="y":
    print("\n"*20)
    play_game()


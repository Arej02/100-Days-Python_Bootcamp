should_continue=True
def find_highest_bidder(bidding_dictionary):
    highest=0
    winner=""
    for i in bidding_dictionary:
        bid_amount=bidding_dictionary[i]
        if bid_amount>highest:
            highest=bid_amount
            winner=i

    print(f"The winner is {winner} with a bid of {highest}")

bids={}
while should_continue:
    name = input("Please enter your name:")
    bid_price = int(input("Please enter you bid price.$"))
    bids[name]=bid_price

    result=input("Do you want to add more bidders.(Yes/No)").lower()
    if result=="no":
        should_continue=False
        find_highest_bidder(bids)
    elif result=="yes":
        print("\n"*20)







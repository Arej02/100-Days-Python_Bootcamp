resources={
    "Water":300,
    "Milk":200,
    "Coffee":100,
}
MENU={
    "Expresso":{
        "ingredients":{
            "Water":50,
            "Milk":0,
            "Coffee":25,
        },
        "cost":1.5
    },
    "Latte":{
        "ingredients":{
            "Water":100,
            "Milk":100,
            "Coffee":25,
        },
        "cost":2.5
    },
    "Cappuccino":{
        "ingredients":{
            "Water":100,
            "Milk":100,
            "Coffee":20,
        },
        "cost":3
    }
}
def is_resource_sufficient(order_ingredients):
    is_enough=True
    for items in order_ingredients:
        if order_ingredients[items]>=resources[items]:
            print(f"Sorry there is not enough {items}.")
            is_enough=False
    return is_enough
def process_coins():
    """"Returns the total calculated from the coins inserted."""
    print("Please insert coins.")
    total=int(input("how many quarters?"))*0.25
    total+= int(input("how many dimes?")) * 0.1
    total+= int(input("how many nickles?")) * 0.05
    total+= int(input("how many pennies?")) * 0.01
    return total
def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is the {change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry not enough money")
        return False
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}")
is_on=True
profit=0
while is_on:
    coffee=input("Enter which coffee do you want?(Expresso,Latte,Cappuccino):")
    if coffee=="Off":
        is_on=False
    elif coffee=="report":
        print(f"Water:{resources['Water']}ml")
        print(f"Milk:{resources['Milk']}ml")
        print(f"Coffee:{resources['Coffee']}ml")
        print(f"Money:${profit}")
    else:
        drink=MENU[coffee]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(coffee,drink["ingredients"])







#from menu import Menu, MenuItem
#from coffee_maker import CoffeeMaker
#from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_maker=MoneyMachine()
menu=Menu()

is_on=True

while is_on:
    option=menu.get_items()
    choice=input("Enter your choice for the coffee:")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_maker.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_maker.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



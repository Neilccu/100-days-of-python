from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while machine_on:
    option = input(f"What would you like? {my_menu.get_items()}\n")
    if option == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif option == "off":
        print("Goodbye")
        machine_on = False
    else:
        drink = my_menu.find_drink(option)

        if drink is not None:
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
                else:
                    print("Error on your payment")
            else:
                print(f"Sorry, not enough resources for {drink.name}")

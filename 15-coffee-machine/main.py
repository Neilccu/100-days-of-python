MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True
money = 0

def report():
    """printing available resources on coffee machine"""
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {money}")

def check_resources(order):
    """Check if the machine has the necessary resources for the requested coffee """
    for ingredient, amount in MENU[order]["ingredients"].items():
        if amount > resources[ingredient]:
            # print(f"Insufficient {ingredient}")
            return False
    return True

def process_coins(order):
    """Ask the user for payment in coins, and return the total amount in dollars"""
    print(f"Please insert {MENU[order]["cost"]}$ in coins or more...")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total

def consume_resources(order):
    """Consume the resource necessaries for the order from the inventory"""
    for ingredient, amount in MENU[order]["ingredients"].items():
        resources[ingredient] -= amount
    return

while machine_on:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "report":
        report()
    elif option == "off":
        machine_on = False
        print("Goodbye!")
    elif option in MENU:
        drink = MENU[option]
        # Single Source of Truth, MENU is the only place where drinks can exist.
        # We can add more later, just using the MENU dictionary
        print(f"You've choose {option}. Processing...")

        if check_resources(option):
            # print(f"Resources available")
            payment = process_coins(option)
            drink_cost = MENU[option]["cost"]

            if payment >= drink_cost:
                change = round(payment - drink_cost, 2)
                if change != 0:
                    print(f"Here is your change: {change}")
                money += drink_cost
                consume_resources(option)
            else:
                print("Sorry, that's not enough money. Money refunded.")

        else:
            print("Sorry, insufficient resources for your order.")

    else:
        print("Please, input a valid option")


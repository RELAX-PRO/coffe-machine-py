"""Coffe machine"""
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
    "money": 0
}
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

while True:
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask == "off":
        break
    elif ask == "report":
        report()
    elif ask == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            if total >= MENU["espresso"]["cost"]:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                resources["money"] += MENU["espresso"]["cost"]
                change = round(total - MENU["espresso"]["cost"],2)
                print(f"Here is ${change} in change.")
                print(f"Here is your espresso ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
    elif ask == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            if total >= MENU["latte"]["cost"]:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["money"] += MENU["latte"]["cost"]
                change = round(total - MENU["latte"]["cost"],2)
                print(f"Here is ${change} in change.")
                print(f"Here is your latte ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
    elif ask == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            if total >= MENU["cappuccino"]["cost"]:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["money"] += MENU["cappuccino"]["cost"]
                change = round(total - MENU["cappuccino"]["cost"],2)
                print(f"Here is ${change} in change.")
                print(f"Here is your cappuccino ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources.")
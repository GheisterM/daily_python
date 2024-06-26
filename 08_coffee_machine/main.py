"""
100 days of python day 15: Make a coffee machine.
"""
import os

COMMANDS = [
    'report',
    'off'
]

COINS = {
    "pennies": 0.01,
    "nickles": 0.05,
    "dimes": 0.1,
    "quarters": 0.25,
}

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
    "money": 0.0,
}


def clear():
    """
    Clears console.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def is_type(typing, value):
    """
    Check if value is of certain type.
    """
    try:
        typing(value)
    except ValueError:
        return False

    return True


def report(res):
    """
    Print resources report with proper format.
    """
    water_str = f"Water: {res['water']}ml\n"
    milk_str = f"Milk: {res['milk']}ml\n"
    coffee_str = f"Coffee: {res['coffee']}g\n"
    money_str = f"Money: ${res['money']}"
    return water_str + milk_str + coffee_str + money_str


def check_resources(new_order, res):
    """
    Check if resources are enough for order.
    Returns if wether the order can be processed or not.
    """
    can_process = True
    for ingredient in MENU[new_order]['ingredients']:
        if res[ingredient] < MENU[new_order]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            can_process = False
            break
    return can_process


def process_coins():
    """
    Asks the user for coins and calculates payment.
    """
    total = 0.0
    for coin in COINS:
        amount = "a"
        while not is_type(int, amount):
            amount = input(f"How many {coin}?: ")
        total += int(amount) * COINS[coin]
    return total


def check_transaction(pay, new_order):
    """
    Checks if payment was enough for transaction.
    Prints message and returns profit.
    """
    change = round(pay - MENU[new_order]["cost"], 2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    elif change > 0:
        print(f"Here is ${change} dollars in change.")

    return change


def make_coffee(new_order, res):
    """
    Makes the coffee and returns left resources.
    """
    for ingredient in MENU[new_order]['ingredients']:
        res[ingredient] -= MENU[new_order]['ingredients'][ingredient]
    print(f"Here is your {new_order}. Enjoy!")
    return res


if __name__ == '__main__':
    for flavor in MENU:
        COMMANDS.append(flavor)

    clear()
    turned_on = True
    while turned_on:
        order = "new"
        while order not in COMMANDS:
            PROMPT = 'What would you like? (espresso/latte/cappuccino):'
            order = input(PROMPT).lower()

        if order == 'off':
            break
        elif order == 'report':
            print(report(resources))
        elif check_resources(order, resources):
            payment = process_coins()
            if check_transaction(payment, order) >= 0:
                resources["money"] += MENU[order]["cost"]
                resources = make_coffee(order, resources)

# Starting code
from cmath import e
import sys
import os
from time import sleep


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
    },
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}


def prompt():

    while True:
        user = input("What would you like to drink? (espresso/latte/cappuccino): ")
        if (
            user != "espresso"
            and user != "latte"
            and user != "cappuccino"
            and user != "off"
            and user != "report"
        ):
            user = input("What would you like to drink? (espresso/latte/cappuccino): ")
        elif user == "off":
            sys.exit()
        elif user == "report":
            report()
        else:
            return user





def report():

    for i in resources:
        if i != "Money":
            print(i, ":", resources[i])
        else:
            print(i + " : $" + str(resources["Money"]))


def isSufficient(drink):

    for i in MENU[drink]["ingredients"]:

        check = MENU[drink]["ingredients"][i]

        if check > resources[i]:
            print(f"Sorry there is not enough {i}")
            sleep(2)
            return False
    return True


def process_coins():
    while True:
        quarters = input("How many quarters do you have? ")
        dimes = input("How many dimes do you have? ")
        nickles = input("How many nickles do you have? ")
        pennies = input("How many pennies do you have? ")
        if (
            quarters.isdigit()
            and dimes.isdigit()
            and nickles.isdigit()
            and pennies.isdigit()
        ):
            sum = (
                (int(quarters) * 0.25)
                + (int(dimes) * 0.10)
                + (int(nickles) * 0.05)
                + (int(pennies) * 0.01)
            )
            result = round(sum, 2)
            return result
        else:
            print("Please enter valid numbers!")


def isTransaction(money, drink):
    if money >= MENU[drink]["cost"]:
        cost = MENU[drink]["cost"]
        change = money - cost
        resources.update({"Money": resources.get("Money") + cost})
        if change != 0:
            print(f"Here is your {round(change,2)} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process(drink):

    for i in MENU[drink]["ingredients"]:

        amount = MENU[drink]["ingredients"][i]
        resources[i] = resources[i] - amount


while True:
    drink = prompt()
    if drink != "report":
        checkSuff = isSufficient(drink)
        if checkSuff:
            money = process_coins()
            if isTransaction(money, drink):
                process(drink)
                print(f"Here is your {drink}. Enjoy!")
                sleep(3)
                os.system("cls")

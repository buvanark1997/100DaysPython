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


def calculate_sum(quarters, dimes, nickles, pennies):
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def compare_rate(sum,user_choice):
    if sum - MENU[user_choice]["cost"] >= 0:
        return f"Here is ${round(sum - MENU[user_choice]['cost'],2)} in change."
    else:
        return "Sorry that's not enough money. Money refunded."


def calculate_supply(user_choice):
    resources["water"] -= MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    if user_choice == "latte" or user_choice == "cappuccino":
        resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]


def enough_supply(user_choice):
    if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
        return "Sorry there is not enough water"
    elif resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
        return "Sorry there is not enough coffee"
    elif user_choice == "latte" or user_choice == "cappuccino":
        if resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
            return "Sorry there is not enough milk"
        else:
            return ""
    else:
        return ""


def coffee_maker():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if enough_supply(user_choice) == "":
        print("Please insert coins.")
        quarters = int(input("how many quarters? "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        sum_value = calculate_sum(quarters, dimes, nickles, pennies)
        print(f"{compare_rate(sum_value,user_choice)}")
        if compare_rate(sum_value,user_choice).__contains__("Money refunded"):
            coffee_maker()
        else:
            print(f"Here is{user_choice} ☕️. Enjoy!")
            coffee_maker()
    else:
        print(f"{enough_supply(user_choice)}")
        coffee_maker()





import string

coffee_drinks = {
    "espresso": {"water_ml": 50, "coffee_g": 18, "milk_ml": 0, "price": 1.50},
    "latte": {"water_ml": 200, "coffee_g": 24, "milk_ml": 150, "price": 2.50},
    "cappuccino": {"water_ml": 250, "coffee_g": 24, "milk_ml": 100, "price": 3.00},
}

machine_resources = {"water_ml": 300, "coffee_g": 100, "milk_ml": 200, "cash": 0.0}


def print_drinks() -> None:
    for i, key in enumerate(coffee_drinks, start=1):
        print(f"{key.title()}: ${coffee_drinks[key]['price']}")


def print_resources():
    print(
        f"Water:  {machine_resources['water_ml']} ml\nCoffee: {machine_resources['coffee_g']} g\nMilk:   {machine_resources['milk_ml']} ml "
    )


def coins_to_cash(pennies: int, nickels: int, dimes: int, quarters: int) -> float:
    return pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25


def make_coffee(drink: str, cash: float) -> tuple[bool, float, str]:
    # check if there's enough stuff in the machine
    change = cash
    if (
        machine_resources["water_ml"] >= coffee_drinks[drink]["water_ml"]
        and machine_resources["coffee_g"] >= coffee_drinks[drink]["coffee_g"]
        and machine_resources["milk_ml"] >= coffee_drinks[drink]["milk_ml"]
        and cash >= coffee_drinks[drink]["price"]
    ):
        machine_resources["water_ml"] -= coffee_drinks[drink]["water_ml"]
        machine_resources["coffee_g"] -= coffee_drinks[drink]["coffee_g"]
        machine_resources["milk_ml"] -= coffee_drinks[drink]["milk_ml"]
        machine_resources["cash"] += coffee_drinks[drink]["price"]

        change = cash - coffee_drinks[drink]["price"]

        return True, change, "Enjoy your coffee!"

    elif coffee_drinks[drink]["price"] > cash:
        return False, change, "Not enough cash."

    else:
        return False, change, "Sorry, we're out of stuff."


def use_coffee_machine():
    is_menu_on = True
    while is_menu_on:
        print("What do you wanna do?")
        print("1. Make coffe")
        print("2. Check Resources")
        print("0. Exit")

        menu_choice = int(input(">"))

        if menu_choice == 0:
            print("Bye")
            break
        elif menu_choice == 1:
            print("What drink do you want?")
            print_drinks()
            drink = input(">")
            drink = drink.lower()

            print("How many pennies?")
            pennies = int(input(">"))
            print("How many nickels?")
            nickels = int(input(">"))
            print("How many dimes?")
            dimes = int(input(">"))
            print("How many quarters?")
            quarters = int(input(">"))

            cash = coins_to_cash(pennies, nickels, dimes, quarters)
            result = make_coffee(drink, cash)
            print(f"{result[2]} Here's your change: {round(result[1],2)}")
            print("")
        elif menu_choice == 2:
            print_resources()
            print("")
        else:
            print("Invalid input")


use_coffee_machine()

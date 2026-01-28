from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creates objects
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()
is_coffee_maker_on = True

while is_coffee_maker_on:
    print("What coffee do you want? (espresso/latte/cappuccino)?")
    print('To turn off - "off" to get report - "report"')
    menu_choice = input(">")

    # TODO turn off by entering "off"
    if menu_choice == "off":
        print("Bye bye!")
        is_coffee_maker_on = False
    elif menu_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
        print("")
    elif menu_choice in my_menu.get_items():
        user_drink = my_menu.find_drink(menu_choice)

        # check if resources are sufficient, process coins
        if my_coffee_maker.is_resource_sufficient(
            user_drink
        ) and my_money_machine.make_payment(user_drink.cost):
            my_coffee_maker.make_coffee(user_drink)
        print("")

import random

difficulty_map = {1: (10, 10), 2: (10, 20), 3: (7, 20), 4: (5, 20), 5: (1, 20)}


def number_guesser(guesses, max_number):
    # generate random number
    gen_number = random.randint(1, max_number)

    is_game_on = True

    while is_game_on:
        print("What's your best guess?")
        user_guess = int(input(">"))

        if guesses == 0:
            is_game_on = False
            print("LOSS!")
            print("")
            break
        elif user_guess == gen_number:
            is_game_on = False
            print("WIN!")
            print("")
            break
        elif user_guess > gen_number:
            print("Your number is larger than mine")
        elif user_guess < gen_number:
            print("Your number is smaller than mine")

        guesses -= 1
        print(f"You have {guesses} left")


def menu():
    is_menu_on = True
    while is_menu_on:
        print("What difficulty do you want?")
        print("1. Baby Mode: 10 guesses - 10 numbers")
        print("2. Easy: 10 guesses - 20 numbers")
        print("3. Medium: 7 guesses - 20 numbers")
        print("4. Hard: 5 guesses - 20 numbers")
        print("5. Impossible: 1 guess - 20 numbers")
        print("0. Exit")

        menu_choice = int(input(">"))

        if menu_choice == 0:
            print("Bye bye!")
            exit()
        elif menu_choice in difficulty_map:
            menu_guesses, menu_max_number = difficulty_map[menu_choice]
            number_guesser(menu_guesses, menu_max_number)
        else:
            print("Invalid choice")
            print("")


menu()

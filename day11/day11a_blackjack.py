import random

# todo: cleanup logic and turn things into functions
cards: list[float] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_game_on = True
dealer_total = 0
player_total = 0

while is_game_on:
    # dealer logic
    if dealer_total <= 17:
        dealer_draw = random.choice(cards)
        if dealer_draw == 11 and dealer_draw + dealer_total > 21:
            dealer_draw = 1

        dealer_total = dealer_total + dealer_draw
        if dealer_total == 21:
            print(f"Dealer win! {dealer_total}")
        elif dealer_total > 21:
            print(f"Dealer bust! {dealer_total}")
            is_game_on = False
        else:
            print(f"Dealer draws {dealer_draw}. Totaling {dealer_total}")

    if is_game_on:
        print("Draw another (y/n)?")
        hit = input(">")

        # player logic
        if hit == "y":
            player_draw = random.choice(cards)
            if player_draw == 11 and player_draw + player_total > 21:
                player_draw = 1

            player_total = player_total + player_draw
            if player_total == 21:
                print(f"Player win! {player_total}")
            elif player_total > 21:
                print(f"Player bust! {player_total}")
                is_game_on = False
            else:
                print(f"Player draws {player_draw}. Totaling {player_total}")

    elif dealer_total >= 17:
        is_game_on = False

    print("#######################")

if player_total == dealer_total:
    print(f"Push (draw) {player_total} = {dealer_total}")
elif 21 > player_total > dealer_total:
    print(f"Player wins! {player_total} > {dealer_total}")
elif 21 > dealer_total > player_total:
    print(f"Dealer wins! {dealer_total} > {player_total}")

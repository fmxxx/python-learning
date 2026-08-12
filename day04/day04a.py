import random

random_int = random.randint(0, 2)

player_pick = int(input("Rock(0), Paper(1), Scissors(2) - SHOOT!"))

if player_pick == random_int:
    print("DRAW!")
elif player_pick == 0 and random_int == 1:
    print("LOSS!")
elif player_pick == 0 and random_int == 2:
    print("WIN!")
elif player_pick == 1 and random_int == 2:
    print("LOSS!")
elif player_pick == 1 and random_int == 0:
    print("WIN!")
elif player_pick == 2 and random_int == 0:
    print("LOSS!")
elif player_pick == 2 and random_int == 1:
    print("WIN!")
else:
    print("Invalid!")

import random
from day07words import words

# sets variables
picked_word = str(random.choice(words))
lives = 10
wrong_guesses = []
# makes display show _ for the size of the picked word
display = []
for i in range(len(picked_word)):
    display.append("_")

game_on = True

while game_on:
    # print display
    display_str = "".join(display)
    print(display_str)
    wrong_guesses_str = "".join(wrong_guesses)
    print("Wrong guesses: " + wrong_guesses_str)
    # win condition
    if display_str == picked_word:
        game_on = False
        print(f"\nYOU WIN! (with {lives} lives)")
        break

    letter = input("Give me a letter\n>")

    # test if input is  more than 1 char
    if len(letter) > 1 or letter == "":
        print("Try again! - Single Letters only")

    # check if inserted letter is in the picked word
    elif letter in picked_word:
        if letter in display:
            print("Guessed Already! Try again")
        else:
            print("You got it!")
            # find where exactly in the string the letter appears, adds it to the display
            for i in range(len(picked_word)):
                if letter == picked_word[i]:
                    display[i] = letter

    else:
        if letter in wrong_guesses:
            print("Guessed Already! Try again")
        else:
            wrong_guesses.append(letter)
            lives = lives - 1
            print(f"Minus one life!! Only {lives} left!!")
        # lose condition
        if lives == 0:
            game_on = False
            print("\nYOU LOSE! The words was: " + picked_word)

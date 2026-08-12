def calculate_love_score(name1: str, name2: str):

    true_count = 0
    love_count = 0

    name1_uppercase: str = str.upper(name1)
    name2_uppercase: str = str.upper(name2)

    for letter in name1_uppercase:
        if letter == "T" or letter == "R" or letter == "U" or letter == "E":
            true_count = true_count + 1
        if letter == "L" or letter == "O" or letter == "V" or letter == "E":
            love_count = love_count + 1

    for letter in name2_uppercase:
        if letter == "T" or letter == "R" or letter == "U" or letter == "E":
            true_count = true_count + 1
        if letter == "L" or letter == "O" or letter == "V" or letter == "E":
            love_count = love_count + 1

    true_love = 10 * true_count + love_count
    print(true_love)


calculate_love_score("Kanye West", "Kim Kardashian")

height = float(input("What's your height - in cm pleaseee?\n"))
age = float(input("What's your age\n"))
photo = input("You want a photo (y/n)?\n")
if age >= 40 and age <= 55:
    midlife_crisis = input("Are you having a midlife crisis (y/n)?\n")

if photo[0] == "y":
    ticket_price = 5
elif photo[0] == "n":
    ticket_price = 0
else:
    print("HUH?")


if height >= 120:
    if age <= 12:
        ticket_price = ticket_price + 10
    elif age <= 18:
        ticket_price = ticket_price + 12
    elif midlife_crisis == "y":
        ticket_price = 0
    else:
        ticket_price = ticket_price + 20
    print(f"Your ticket will be ${ticket_price}")
else:
    print("I SMITHE THEE!")

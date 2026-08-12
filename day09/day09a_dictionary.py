bidders_list = {}

over = False
while over == False:
    input_name = input("Name\n>")
    input_bid = float(input("Bid\n>"))
    bidders_list[input_name] = input_bid

    keep_going = input("Continue (y/n)?\n>")
    if keep_going == "n":
        over = True
    print("\n" * 100)

largest = 0
winner = ""
for key, value in bidders_list.items():
    print(f"{key}: {value}")
    if value > largest:
        largest = value
        winner = key

print("WINNER:")
print(f"{winner} with a bid of {largest}")

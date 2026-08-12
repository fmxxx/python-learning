size = input("What size (s,m,l)\n")
pepperoni = input("Pepperoni (y/n)?\n")
chesse = input("Extra chesse (y/n?\n")

if size == "s":
    total = 15
    if pepperoni == "y":
        total = total + 2
if size == "m":
    total = 20
    if pepperoni == "y":
        total = total + 3
if size == "l":
    total = 25
    if pepperoni == "y":
        total = total + 3
if chesse == "y":
    total = total + 1
else:
    print("whaaat")

print(f"Total: ${total}")

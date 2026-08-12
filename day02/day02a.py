text_index = input("What nth letter of the text you want? (0 index)\n")
text_index = int(text_index)

text = "Lorem ipsum"
if text_index > (len(text)):
    print("too high numberr :(")
else:
    print(f"The {text_index},th char in {text} is: {text[text_index]}")

print("\n")
print("Round and floor test")
decimal_number = 4.9849465118
print(decimal_number)
print(f"Rounded, 2 decimals = {round(decimal_number, 2)}")
print(f"Floor = {int(decimal_number)}")

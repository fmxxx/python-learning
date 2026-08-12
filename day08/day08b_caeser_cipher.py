# menu
# - encode
# - decode

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

symbols = [
    " ",
    ",",
    ".",
    "!",
    "?",
    "#",
    "$",
    "%",
    "&",
    "'",
    '"',
    "(",
    ")",
    "*",
    "+",
    "-",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
]


def caeser_cipher(phrase: str, shift: int, direction: int):
    encoded: list[str] = []
    for letter in phrase:
        if letter in alphabet:
            alpha_pos = alphabet.index(letter)
            # direction -> 1 = encode, -1 = decode
            # % 26 makes it wrap around to a (0)  when it goes past z (25)
            shifted_pos = (alpha_pos + shift * direction) % 26
            encoded.append(alphabet[shifted_pos])
        elif letter in symbols:
            encoded.append(letter)
        else:
            raise SystemExit(f"Invalid character: '{letter}'")

    encoded_str = "".join(encoded)
    print("\n" + encoded_str)


# main
input_phrase: str = ""
input_shift: int = 0
run = True

while run:
    print("1. Encode")
    print("2. Decode")
    print("0. Quit")
    menu = int(input(">"))

    if menu == 1:
        input_phrase = input("String to encode\n>")
        input_shift = int(input("Shift amount\n>"))
        caeser_cipher(input_phrase, input_shift, 1)
    elif menu == 2:
        input_phrase = input("String to decode\n>")
        input_shift = int(input("Shift amount\n>"))
        caeser_cipher(input_phrase, input_shift, -1)
    else:
        run = False
        print("Bye!")
    print("")

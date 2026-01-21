import random

lowercase = [
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
uppercase = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]
all_chars = [lowercase, uppercase, numbers, symbols]


amt_lowercase = int(input("How many lowercase?\n"))
amt_uppercase = int(input("How many uppercase?\n"))
amt_numbers = int(input("How many numbers?\n"))
amt_symbols = int(input("How many symbols?\n"))

amt_total = amt_lowercase + amt_uppercase + amt_numbers + amt_symbols

""" Better way
password_pool = []
password_pool.extend(random.choices(lowercase, k=amt_lowercase))
password_pool.extend(random.choices(uppercase, k=amt_uppercase))
password_pool.extend(random.choices(numbers, k=amt_numbers))
password_pool.extend(random.choices(symbols, k=amt_symbols))
"""
password_pool = []
for char in range(0, amt_lowercase):
    password_pool.append(random.choice(lowercase))
for char in range(0, amt_uppercase):
    password_pool.append(random.choice(uppercase))
for char in range(0, amt_numbers):
    password_pool.append(random.choice(numbers))
for char in range(0, amt_symbols):
    password_pool.append(random.choice(symbols))


random.shuffle(password_pool)

password = "".join(password_pool)
print(password)

"""My way (dumb)
password = ""
for i in range(0, amt_total):
    pick = random.randint(0, (len(password_pool) - 1))
    password += password_pool[pick]
    password_pool.pop(pick)

print(password)
# 2
# Randomly sample all items (this shuffles them)
password_chars = random.sample(password_pool, len(password_pool))
password = "".join(password_chars)
print(password)

# 3
# Shuffle and join
random.shuffle(password_pool)
password = "".join(password_pool)
print(password)

# 4
password = "".join(
    random.choices(lowercase, k=amt_lowercase)
    + random.choices(uppercase, k=amt_uppercase)
    + random.choices(numbers, k=amt_numbers)
    + random.choices(symbols, k=amt_symbols)
)
password = "".join(random.sample(password, len(password)))
print(password)
"""

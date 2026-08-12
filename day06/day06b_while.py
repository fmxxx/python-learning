import random

count = 0
x = True
while x == True:
    print(f"True{count}")
    if random.randint(0, 10) == 1:
        x = False
    count += 1

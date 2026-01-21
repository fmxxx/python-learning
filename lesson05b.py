# loops in ranges
# somar todos numeros de 1 a 100

# gauss way (just cuz)
result = 0
for i in range(1, 51):
    result += i + (101 - i)

print(result)

# normal way
result = 0
for i in range(1, 101):
    result += i

print(result)

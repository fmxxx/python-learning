fruits = ["Apple", "Banana", "Cherry", "Dragonfruit"]

# loop in a list (fruit is a string)
for fruit in fruits:
    print(fruit)


scores = [10, 70, 80, 90, 55, 62, 66, 67, 67, 84, 11, 22, 54, 59]

sum_scores = 0
for score in scores:
    sum_scores += score

print(sum_scores)

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score

print(max_score)

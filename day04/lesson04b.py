import random

list_of_stuff = ["milk", "eggs", "meat", "potatoes", "bananas", "juice"]

# get first
print(list_of_stuff[0])
# get last
print(list_of_stuff[-1])
# add to end
list_of_stuff.append("candy")
print(list_of_stuff)
# add lots of stuff to end
list_of_stuff.extend(["stuff", "more stuff"])
print(list_of_stuff)
# random item
random_item = list_of_stuff[random.randint(0, len(list_of_stuff))]
print(random_item)
# better way
print(random.choice(list_of_stuff))

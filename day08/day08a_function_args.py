def greet(name: str, age: float):
    print("How are you, " + name + "?")
    print(f"You look young for {age}. What's your skincare routine?")


name: str = input("Hello! What's your name\n>")
age: int = int(input("What's your age?\n>"))

greet(name, age)
print("")
# static with keyword args
greet(name="John", age=30)

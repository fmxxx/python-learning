def my_func():
    print("My")
    print("Function")


def hello_times(a: int):
    for i in range(a + 1):
        print(f"Hello{i}")


my_func()

hello_times(int(input("How many times?")))

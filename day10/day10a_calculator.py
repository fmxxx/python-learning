def add(x: float, y: float) -> float:
    result: float = x + y
    return result


def subtract(x: float, y: float) -> float:
    result: float = x - y
    return result


def multiply(x: float, y: float) -> float:
    result: float = x * y
    return result


def divide(x: float, y: float) -> float:
    result: float = x / y
    return result


def power(x: float, y: float) -> float:
    result: float = x**y
    return result


def calculator():
    # dynamically changes what operations you can choose
    operations_map = {"+": add, "-": subtract, "*": multiply, "/": divide, "^": power}
    available_operators = ""
    available_operators = " ".join(operations_map.keys())

    is_calculator_on = True
    first_number = float(input("First Number\n>"))

    while is_calculator_on:

        operation_character = input("Operation " + available_operators + " \n>")
        second_number = float(input("Second Number\n>"))

        selected_function = operations_map[operation_character]
        current_result = selected_function(first_number, second_number)

        print(current_result)
        print("")

        should_continue = input(f"Continue with {current_result} (y/n)\n>")
        if should_continue == "n":
            is_calculator_on = False
            print("Bye")
        else:
            first_number = current_result


calculator()

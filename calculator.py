def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first / second


def main():
    operations = {
        "1": ("Addition", add, "+"),
        "2": ("Subtraction", subtract, "-"),
        "3": ("Multiplication", multiply, "*"),
        "4": ("Division", divide, "/"),
    }

    print("Simple Calculator")
    for number, (name, _, _) in operations.items():
        print(f"{number}. {name}")

    choice = input("Choose an operation (1-4): ").strip()
    if choice not in operations:
        print("Invalid operation.")
        return

    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        _, operation, symbol = operations[choice]
        result = operation(first, second)
    except ValueError:
        print("Please enter valid numbers.")
        return
    except ZeroDivisionError as error:
        print(error)
        return

    print(f"{first:g} {symbol} {second:g} = {result:g}")


if __name__ == "__main__":
    main()
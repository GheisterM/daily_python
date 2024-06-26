import os, art

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def validate_number(position):
    result = None
    while result is None:
        try:
            result = float(input(f"What's the {position} number? "))
        except ValueError:
            result = None

    return result

def calculator():
    print(art.logo)
    operations = {}

    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
    }

    num1 = validate_number("first")
    cont = "y"
    while cont == "y":
        symbol = ""
        while symbol not in operations.keys():
            symbol = input("What operation you want to do (" + ", ".join(operations) + ")? ")
        num2 = validate_number("next")
        calculation_function = operations[symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {symbol} {num2} = {result}")

        cont = ""
        while cont not in ("y", "n"):
            cont = input(f"Do you want to continue calculating with {result} (y) or start again (n)?\n")
            num1 = result

    clear()
    calculator()


if __name__ == "__main__":
    calculator()
from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def  divide(n1, n2):
    return n1 / n2



calculator_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

continue_program = True
result = ""
first_number = float(input("What's the first number?: "))

while continue_program:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = calculator_functions[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    user_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if user_continue == "y":
        first_number = result
    else:
        continue_program = False

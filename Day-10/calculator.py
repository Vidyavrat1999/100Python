from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


num1 = float(input("What is the first number: "))
should_accumulate = True

while should_accumulate:
    for symbol in operations:
        print(symbol)
    operation = input("Choose an operation: ")
    num2 = float(input("Whats second number: "))
    answer = operations[operation](num1, num2)
    print(num1, operation, num2, "=", answer)

    choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to reset calculator.\n").lower()

    if choice == "y":
        num1 = answer
    else:
        should_accumulate = False

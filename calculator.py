# Calculator

def get_inputs():
    while True:
        op = input(
            "Enter the op you want to perform (add, subtract, multiply, divide, q to quit): ")
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        try:
            number1 = float(num1)
            number2 = float(num2)
            return op, number1, number2
        except ValueError:
            print("Please enter valid numbers.\n")


# Get inputs from user
op, number1, number2 = get_inputs()

while True:
    if op.lower() in ["q", "quit"]:
        print("Exiting the calculator. Goodbye!")
        break

    elif op.lower() == "add":
        result = number1 + number2
        print(
            f"The result of adding {number1} and {number2} is: {result:.2f}")

    elif op.lower() == "subtract":
        result = number1 - number2
        print(
            f"The result of subtracting {number2} from {number1} is: {result:.2f}")

    elif op.lower() == "multiply":
        result = number1 * number2
        print(
            f"The result of multiplying {number1} and {number2} is: {result:.2f}")

    elif op.lower() == "divide":
        while True:
            try:
                result = number1 / number2
                print(
                    f"The result of dividing {number1} by {number2} is: {result:.2f}")
                break
            except ZeroDivisionError:
                print("Cannot divide by zero. Please enter a valid second number.")
                number2 = float(input("Enter the second number again: "))

    else:
        print("Invalid operation.")

    recal = input("Do you want to calculate once again?(yes/no)")
    if recal.lower() != "yes":
        print("Closing the calculator")
        break

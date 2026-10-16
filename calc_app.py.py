def calculate():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("enter an operation (+, -, *, /): ")

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2 
        elif operation == "*":
            answer = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: You cannot divide bt zero.")
                return
            answer = num1 / num2
        else:
            print("Error: Invalid operation.")
            return

        equation = f"{num1:g} {operation} {num2:g} = {answer:g}"

        print("Answer: ", answer)

        with open("equations.txt", "a") as file:
            file.write("equation + \n")

    except ValueError:
        print("Error: Please enter valid numbers.")

def print_equations():
    try:
        with open("equations.txt", "r") as file:
            equations = file.read()

        if equations:
            print("\nPrevious equations:")
            print(equations)
        else:
            print("No previous equations found.")

    except FileNotFoundError:
        print("No previous equations found.")

while True:
    print("\nCalculator")
    print("1. Perform a calculation")
    print("2. Print previous equations")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculate()
    elif choice == "2":
        print_equations()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Error: Please choose 1, 2 or 3.")
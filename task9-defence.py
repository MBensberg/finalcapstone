import operator
import os

def perform_operation(operator_symbol, num1, num2):
    # Dictionary mapping operator symbols to corresponding functions
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    if operator_symbol in operations:
        operation_func = operations[operator_symbol]
        return operation_func(num1, num2)
    else:
        return None

def write_equation_to_file(equation, file_name):
    with open(file_name, 'a') as file:
        file.write(equation + '\n')

def calculate_equation(num1, operator_symbol, num2, file_name=None):
    try:
        result = perform_operation(operator_symbol, num1, num2)
        if result is None:
            print("Invalid operator symbol. Please try again.")
            return
        equation = f"{num1} {operator_symbol} {num2} = {result}"
        print(equation)
        if file_name:
            write_equation_to_file(equation, file_name)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

def calculate_equations_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            equations = file.readlines()
        for equation in equations:
            equation = equation.strip()
            equation_parts = equation.split()
            if len(equation_parts) == 3:
                try:
                    num1, operator_symbol, num2 = equation_parts
                    num1 = float(num1)
                    num2 = float(num2)
                    calculate_equation(num1, operator_symbol, num2)
                except ValueError:
                    print(f"Invalid number in equation: {equation}")
            else:
                print(f"Invalid equation format: {equation}")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")

def start_calculator():
    print("Welcome to the Calculator!")
    print("Please select an option:")
    print("1. Perform calculation with two numbers")
    print("2. Perform calculations from a file")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        try:
            num1 = float(input("Enter the first number: "))
            operator_symbol = input("Enter the operator symbol (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            calculate_equation(num1, operator_symbol, num2, file_name='equations.txt')
        except ValueError:
            print("Invalid number entered.")
    elif choice == '2':
        file_name = input("To read all past equations from a text file please TYPE the following file name: equations.txt\n")
        calculate_equations_from_file(file_name)
    elif choice == '3':
        print("Thank you for using the Calculator. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
    print()
    start_calculator()

# Start the calculator
start_calculator()

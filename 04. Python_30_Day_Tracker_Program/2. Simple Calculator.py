print('\t\t"Welcome to Simple Calculator Program !!"')

# Input for num1
while True:
    try:
        num1 = float(input('Please enter the first number: '))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Input for num2
while True:
    try:
        num2 = float(input('Please enter the second number: '))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

operation = input('Please enter the operation (+, -, *, /): ')

if operation not in ['+', '-', '*', '/']:
    print("Invalid operation selected.")
else:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        print(f"The result of {num1:.2f} {operation} {num2:.2f} is: {result:.2f}")

input('Press Enter to exit...')

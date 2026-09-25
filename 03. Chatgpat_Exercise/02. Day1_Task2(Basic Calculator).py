print('\t\t "Welcome to Basic Calculator!" \t\t')
try:
    Num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print('\t\t "Please select the operation you want to perform: " \t\t')
    print("+. Addition")
    print("-. Subtraction")
    print("*. Multiplication")
    print("/. Division")
    print("%. Modulus")
    Operation = input("Enter the operation you want to perform: ")
    if Operation == "+":
        Result = Num1 + num2
        print(f"The result of the addition is: {Result:.2f}")
    elif Operation == "-":
        Result = Num1 - num2
        print(f"The result of the subtraction is: {Result:.2f}")
    elif Operation == "*":
        Result = Num1 * num2
        print(f"The result of the multiplication is: {Result:.2f}")
    elif Operation == "/":
        if num2 != 0:
            Result = Num1 / num2
            print(f"The result of the division is: {Result:.2f}")
        else:
            print("Error: Division by zero is not allowed.")
    elif Operation == "%":
        if num2 != 0:
            Result = Num1 % num2
            print(f"The result of the modulus is: {Result:.2f}")
        else:
            print("Error: Modulus by zero is not allowed.")
    else:
        print("Invalid operation selected. Please select a valid operation.")
except ValueError:
    print("\n\t\tInvalid input! Please enter a valid number. \t\t")
print("\n\t\tThank You For Using The Basic Calculator! \t\t")
end = input("Press Enter to exit the program.")
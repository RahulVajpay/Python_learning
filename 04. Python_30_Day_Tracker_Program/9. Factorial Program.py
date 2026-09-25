print('\t\t"Welcome to the Factorial Calculator!"')
while True:
    try:
        num1 = int(input("Enter a number to calculate its factorial: "))
        if num1 < 0:
            print("Factorial is not defined for negative numbers.")
            continue
        elif num1 == 0 or num1 == 1:
            print(f"The factorial of {num1} is: 1")
        else:
            i = 1
            factorial = 1
            while i <= num1:
                factorial *= i
                i += 1
            print(f"The factorial of {num1} is: {factorial}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
end = input("Press Enter to exit the program...")

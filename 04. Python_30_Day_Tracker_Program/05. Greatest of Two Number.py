print('\t\t"Welcome to Greatest of Two Number!"')
while True:
    try:
        num1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
while True:
    try:
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if num1 > num2:
    print(f"{num1:.2f} is greater than {num2:.2f}.")
elif num2 > num1:
    print(f"{num2:.2f} is greater than {num1:.2f}.")
else:
    print("Both numbers are equal.")
end = input("Press Enter to exit the program.")

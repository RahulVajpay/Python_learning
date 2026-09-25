print('\t\t "Welcome to Number Swapping!" \t\t')
# Taking input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"\nBefore swapping: First = {num1}, Second = {num2}")

    # Swapping the numbers
    temp = num1     # Storing the first number in a temporary variable
    num1 = num2     # Assigning the value of the second number to the first number
    num2 = temp     # Assigning the value stored in the temporary variable to the second number
    # Displaying the swapped numbers
    print(f"After swapping: First number = {num1}, Second number = {num2}")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
print('\t\t "Thank you for using Number Swapping!" \t\t')
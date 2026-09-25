print('\t\t"Welcome to the Swap Two Numbers Program!"')
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

print (f"before swapping: First number = {num1:.2f}, Second number = {num2:.2f}")
temp = num1
num1 = num2
num2 = temp
print (f"after swapping: First number = {num1:.2f}, Second number = {num2:.2f}")
end = input("Press Enter to exit the program.")


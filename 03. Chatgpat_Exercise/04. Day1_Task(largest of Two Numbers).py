print('\t\t"Welcome to Largest of Two Numbers Checker!" \t\t')
try:
    Num1 = float(input("Enter the first number: "))
    Num2 = float(input("Enter the second number: "))
    if Num1 > Num2:
        print(f"\n The largest number is: {Num1}")
    elif Num2 > Num1:
        print(f"\n The largest number is: {Num2}")
    else:
        print(f"\n Both numbers are equal: {Num1}")
    print("\n\t\tThank You For Using The Largest of Two Numbers Checker! \t\t")
except ValueError:
    print("\n\t\tInvalid input! Please enter a valid number. \t\t")
end = input("Press Enter to exit the program.")
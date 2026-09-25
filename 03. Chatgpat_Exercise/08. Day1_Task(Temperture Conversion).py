print('\t\t "Welcome to Temperature Conversion!" \t\t')
try:
    temp = float(input("Enter the temperature you want to convert: "))
    print('\t\t "Please select the conversion you want to perform: " \t\t')
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")
    conversion = input("Enter the conversion you want to perform (1-6): ")
    if conversion == "1":
        result = (temp * 9/5) + 32
        print(f"The result of the conversion is: {result:.2f} °F")
    elif conversion == "2":
        result = (temp - 32) * 5/9
        print(f"The result of the conversion is: {result:.2f} °C")
    elif conversion == "3":
        result = temp + 273.15
        print(f"The result of the conversion is: {result:.2f} K")
    elif conversion == "4":
        result = temp - 273.15
        print(f"The result of the conversion is: {result:.2f} °C")
    elif conversion == "5":
        result = (temp - 32) * 5/9 + 273.15
        print(f"The result of the conversion is: {result:.2f} K")
    elif conversion == "6":
        result = (temp - 273.15) * 9/5 + 32
        print(f"The result of the conversion is: {result:.2f} °F")
    else:
        print("Invalid conversion selected. Please select a valid conversion.")
except ValueError:
    print("\n\t\tInvalid input! Please enter a valid number. \t\t")
print("\n\t\tThank You For Using The Temperature Conversion! \t\t")
end = input("Press Enter to exit the program.")
print('\t\t"Welcome to Simple Interest Calculator!"')
while True:
    try:
        PA = float(input("Enter the principal amount: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the principal amount.")
while True:    
    try:
        R = float(input("Enter the rate of interest (in percentage): "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the rate of interest.")
while True:
    try:
        T = float(input("Enter the time period (in years): "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the time period.")
SI = (PA * R * T) / 100
print(f"Your money will grow with ROI {R:.2F}% in {T} years: {SI:.2f}")
print(f"Total amount after {T} years will be: {PA + SI:.2f}")
end = input("Press Enter to exit the program.")
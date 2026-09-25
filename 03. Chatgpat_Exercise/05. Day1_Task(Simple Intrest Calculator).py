print('\t\t Welcome to Simple Interest Calculator! \t\t')
try:
    PA = float(input("Please Enter your Principal Amount : "))
    RA = float(input("Please Enter your yearly Rate of Interest : "))
    TI = float(input("Please Enter your Time Period in Years: "))

    SI = (PA * RA * TI)/100
    print(f"\nYou Will earn a Simple Interest of: Rs.{SI:.2f}")
    print(f"Your Total Amount after {TI} years will be: Rs.{(PA + SI):.2f}")
    print("\n\t\tThank You For Using The Simple Interest Calculator! \t\t")
    end = input("Press Enter to exit the program.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
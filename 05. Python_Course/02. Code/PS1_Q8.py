print("Welcome to Basic Sqaure and Cube Finding Program.")
while True:
    try:
        num1 = int(input("Please Enter your Number Which Square and Cube is Need to Find. : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")
print(f"Square of {num1} = {num1**2}")
print(f"Cube   of {num1} = {num1**3}")
end = input("Press Enter to Exit the Program...")
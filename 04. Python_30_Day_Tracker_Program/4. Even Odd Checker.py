print('\t\t"Welcome to Even Odd Checker!"')
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
end = input("Press Enter to exit the program.")
# Q 1.3 Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.
# Solution ==>

print('Welcome to Odd Even Check Program.')
while True:
    try:
        num1 = int(input("Please Enter your Number to Check."))
        break
    except ValueError:
        print("Please Enter a Valid Number to Check.")
if num1 % 2 == 0:
    print(f"{num1} is an Even Number.")
elif num1 % 2 != 0:
    print(f"{num1} is an Odd Number.")
end = input("Press Enter to Exit the Program...")
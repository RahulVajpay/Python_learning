# Q 1.1 Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
# Solution ==>

print('Welcome to Number Check Program.')
while True:
    try:
        num1 = int(input("Please Enter your Number to Check."))
        break
    except ValueError:
        print("Please Enter a Valid Number to Check.")
if num1 > 0:
    print(f"{num1} is a Positive Number.")
elif num1 <0:
    print(f"{num1} is a Negative Number.")
else:
    print("Nice You have Entered Zero")
end = input("Press Enter to Exit the Program...")
# Q 2.2 Write a program using match case that simulates a simple calculator. Ask the user for two numbers and an operation (+, -, *, /).Perform the operation using match case ?
# Solution ==>

print("Welcome to Basic Calculator.")
while True:
    try:
        num1 = float(input("Please Enter Your First Number   : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")
while True:
    try:
        num2 = float(input("Please Enter Your Second Number. : "))
        if num2 ==0:
            print("Please Enter a Number greater than Zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Valid Number.")
Operation = input("Please Select a Operation (+, -, *, /).")
match Operation :
    case "+" :
        print(f"{num1} {Operation} {num2} = {num1 + num2}")
    case "-" :
        print(f"{num1} {Operation} {num2} = {num1 - num2}")
    case "*" :
        print(f"{num1} {Operation} {num2} = {num1 * num2}")
    case "/" :
        print(f"{num1} {Operation} {num2} = {num1 / num2}")
    case _:
        print("You Have Selected a Wrong Operation.")
print("Thanks for using Basic Calculator.")
end = input("Press Enter to Exit the Program.")




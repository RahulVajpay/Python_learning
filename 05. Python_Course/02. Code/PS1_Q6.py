print("Welcome to Simple Calculator Program.")
while True:
    try:
        num1 = int(input("Please Enter your First Number.  : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")
while True:
    try:
        num2 = int(input("Please Enter your Second Number. : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} x {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')

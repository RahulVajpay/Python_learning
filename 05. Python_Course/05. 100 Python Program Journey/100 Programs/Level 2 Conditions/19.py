# 19. Simple Calculator using if-else
# Solution ==>

def greet():
    print("Welcome to Simple Opertaion Calculator.")

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Division With Zero is Not Possible."
    else:
        return a/b

while True: 
    try:
        num1 = float(input("Please Enter your First Number."))
        break
    except ValueError:
        print("Please Enter a Valid Number.")

print(''' Please Enter Your Choice As Per Below.
"+" For Add
"-" For Substraction
"*" For Multiplication
"/" For Division                        
''')
while True:
    try:
        operation = input("Please Enter your Opertaion : ")
        if operation in ("+", "-", "*", "/"):
            break
    except ValueError:
        print("Please Enter a Valid Operation.")

while True: 
    try:
        num2 = float(input("Please Enter your Second Number."))
        break
    except ValueError:
        print("Please Enter a Valid Number.")

if operation == "+":
    print(f"{num1} {operation} {num2} = {sum(num1, num2)}")
elif operation == "-":
    print(f"{num1} {operation} {num2} = {sub(num1, num2)}")
elif operation == "*":
    print(f"{num1} {operation} {num2} = {mul(num1, num2)}")
elif operation == "/":
    print(f"{num1} {operation} {num2} = {div(num1, num2)}")
else:
    print("Please Enter a Valid Operation.")    
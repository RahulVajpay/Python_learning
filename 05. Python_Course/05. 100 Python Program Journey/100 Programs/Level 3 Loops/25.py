# 25. Factorial using loop.
# Solution ==>

def greet ():
    print("Welcome to Factorial Calulator.")

def _Factorial (num):
    if num == 0:
        return 1
    i = 1
    Fact = 1
    while i <= num:
        Fact *= i
        i +=1
    return Fact

greet()
while True:
    try:
        num1 = int(input("Please Enter a Number which factorial you want to Calculate. : "))
        if num1 < 0:
            print("Number should be a Positive Integer.")
        else:
            break    
    except ValueError:
        print("Please Enter a Valid Number.")

print(f"The Factorial of {num1} is {_Factorial(num1)}.")
# 27. Reverse a number
# Solution ==>

def greet ():
    print("Welcome to Number Reverse Program.")

def _reversenum(num):
    absnum = abs(num)
    revnum = 0
    while absnum > 0:
       revnum = revnum * 10 + (absnum%10)
       absnum //=10
    if num  >= 0:   
       print(f"The reverse Number of {num} is {revnum} ")
    else:   
       print(f"The reverse Number of {num} is {revnum*-1} ")

greet()
while True:
    try:
        num1 = int(input("Please Enter a Number which you want to Reverse. : "))
        break    
    except ValueError:
        print("Please Enter a Valid Number.")

_reversenum(num1)
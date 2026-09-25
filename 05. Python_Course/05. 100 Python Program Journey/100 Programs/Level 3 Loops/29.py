# 29. Armstrong Number
# Solution ==>

def greet ():
    print("Welcome to Armstrong Number Check Program.")

def _digitCount(num):
    _absnum = abs(num)
    i = 1
    count = 0
    while _absnum > 0:
       _absnum //=10
       count +=1
    return count   


def Armstrong(num1):
    absnum = abs(num1)
    Armnum = 0
    numDigits = _digitCount(num1)
    while absnum > 0:
       Armnum = (absnum%10)**numDigits + Armnum
       absnum //=10
    if num1 == Armnum:   
       print(f"{num1} is a Armstrong Number.")
    elif num1 != Armnum:   
       print(f"{num1} is Not Armstrong Number.")   

greet()
while True:
    try:
        num1 = int(input("Please Enter a Number which you want to Check. : "))
        if num1 <= 0:
            print("Number Should not be Zero or Negative.")
        else:
            break    
    except ValueError:
        print("Please Enter a Valid Number.")

Armstrong(num1) 
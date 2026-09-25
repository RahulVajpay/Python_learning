# 32. Find LCM of two numbers
# Solution ==>

print("Welcome to LCM Of Numbers Find Program.")
while True:
    try:
        num1 = int(input("Please Enter your First Number : "))
        if num1 <= 0:
            print("Number Should not be Zero or Negative.")
        else:
            break    
    except ValueError:
        print("Please Enter a Valid Number.")
while True:
    try:
        num2 = int(input("Please Enter your Second Number : "))
        if num2 <= 0:
           print("Number Should not be Zero or Negative.")
        else:
            break    
    except ValueError:
        print("Please Enter a Valid Number.")

_orignum1 = num1
_orignum2 = num2

if num1 > num2:
    while True:
        if num1%num2 ==0:
            print(f"LCM of {_orignum1} and {_orignum2} is {num1}")
            break
        else:
            i = 2
            while i <= num2:
                num1 = _orignum1*i
                if  num1%num2 == 0:
                    print(f"LCM of {_orignum1} and {_orignum2} is {num1}")
                    break
                else:
                    i+=1
else:
    while True:
        if num2%num1 ==0:
            print(f"LCM of {_orignum1} and {_orignum2} is {num2}")
            break
        else:
            i = 2
            while i<=num1:
                num2 = _orignum2*i
                if  num2%num1 == 0:
                    print(f"LCM of {_orignum1} and {_orignum2} is {num2}")
                    break
                else:
                    i+=1





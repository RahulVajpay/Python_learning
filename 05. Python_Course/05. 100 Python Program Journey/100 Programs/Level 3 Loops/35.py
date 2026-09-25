# 35. Prime Number Checker
# Solution

print("Welcome to Prime number Check Program !!")

while True:
    try:
        num1 = int(input("Please Enter your Number. "))
        if num1 <=0:
            print("Please Enter a Positive number Greater than Zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Valid Number.")
if num1 == 1:
    print(f"{num1} is neither Prime nor Composite.")
elif num1 == 2 or num1 == 3 or num1 == 5:
    print(f"You have Entered {num1} which is a Prime Number.")    
elif num1%2 ==0 or num1%3==0 or num1%5 ==0:
    print(f"Your Number {num1} is Not a Prime Number.")    
else:    
    _DivisorList = []
    i = 2
    while i <= round((num1**0.5+1), 0):
        if num1%i == 0:
            _DivisorList.append(i)
            if len(_DivisorList)>2:
                break
            else:
                i+=1
        else:
            i+=1
    if len(_DivisorList)>2:
        print(f"You Number {num1} is Not a Prime number and its First three Divisior is {_DivisorList}")
    else:
         print(f"Your Number {num1} is a Prime Number.")    



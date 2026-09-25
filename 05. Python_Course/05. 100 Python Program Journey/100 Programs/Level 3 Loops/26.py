# 26. Count digits in a number
# Solution ==>

def greet ():
    print("Welcome to Digit Count Calulator.")

def _digitCount(num):
    if num == 0:
        print(f"The Number of digit in {num} is 1 ")
        return
    else:
        _absnum = abs(num)
        count = 0
        while _absnum > 0:
           _absnum //=10
           count +=1
        if num > 0:   
           print(f"The Number of digit in {num} is {count} ")
        else:
            print(f"The Number of digit in {num} is {count} ")
        return                

greet()
while True:
    try:
        num1 = int(input("Please Enter a Number which Digit you want to Count : "))
        break    
    except ValueError:
        print("Please Enter a Valid Number.")

_digitCount(num1)

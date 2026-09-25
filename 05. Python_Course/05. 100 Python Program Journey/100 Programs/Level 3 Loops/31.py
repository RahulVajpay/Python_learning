# 31. Find GCD of two numbers
# Solution ==>

def greet():
    print("Welcome to Greatest Common Divisor (GCD) Program.")

def GCD (_NUMBER):
    _sortNum = sorted(_NUMBER)
    if _sortNum[1]%_sortNum[0] == 0:
        return _sortNum[0]
    else:
        reminder = None
        while _sortNum[1]%_sortNum[0] > 0:
            reminder = _sortNum[1]%_sortNum[0]
            _sortNum.pop()
            _sortNum.append(reminder)
            _sortNum.sort()
            return GCD(_sortNum)


_number = []
greet()
while True:
    try:
        num1 = int(input("Please Enter your First Number : "))
        if num1 <= 0:
            print("Number Should not be Zero or Negative.")
        else:
            _number.append(num1)
            break    
    except ValueError:
        print("Please Enter a Valid Number.")
while True:
    try:
        num2 = int(input("Please Enter your Second Number : "))
        if num2 <= 0:
           print("Number Should not be Zero or Negative.")
        else:
            _number.append(num2)
            break    
    except ValueError:
        print("Please Enter a Valid Number.")

print(f"GCD of {num1} and {num2} is {GCD(_number)}")
            



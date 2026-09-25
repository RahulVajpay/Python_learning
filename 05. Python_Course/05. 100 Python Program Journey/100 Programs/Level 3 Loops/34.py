# 34. Print all odd numbers in range
# Solution ==>

print("Welcome to Odd Numbers Find Program in a Range..")
while True:
    try:
        num1 = int(input("Please Enter your Range First Number : "))
        break    
    except ValueError:
        print("Please Enter a Valid Number.")
while True:
    try:
        num2 = int(input("Please Enter your Range Second Number : "))
        if num2 < num1:
           print("Second Numbers Should be Graeter than First Number.")
        else:
            break    
    except ValueError:
        print("Please Enter a Valid Number.")

origNum = num1
_odd = []

while num1 <= num2:
    if num1%2!=0:
        _odd.append(num1)
        num1 +=1
    else:
        num1 +=1

print(f"The odd Numbers Between {origNum} and {num2} = {_odd}")

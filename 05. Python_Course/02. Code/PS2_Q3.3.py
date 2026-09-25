# Q 3.1 Calculate the sum of all numbers from 1 to 100 using a for Loop.
# Solution.==>

print("Welcome to Sum of N numbers Print Progam in a Range")
while True:
    try:
        start_Num = int(input("Please Enter your Series Start Number. : "))
        if start_Num < 0:
            print("Please Enter a Positive Number.")
        else:
            break
    except ValueError:
        print("Please Enter a Valid Number.")
while True:
    try:
        end_Num = int(input("Please Enter your Series End Number. : "))
        if end_Num > start_Num:
            break
        else:
            print("Please Enter a Number Greater than Your Series Start Number.")
    except ValueError:
        print("Please Enter a Valid Number.")
total = 0
rangestartNum = start_Num
for start_Num in range(start_Num, (end_Num + 1)):
     total += start_Num
     start_Num +=1
print(f"The Sum of Number Between {rangestartNum} and {end_Num} is {total}")
end = input("Thanks for Using Program. Please Press Enter to Exit the Program.")

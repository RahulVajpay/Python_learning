# Q 4.1 Print numbers from 1 to 10 using a while loop.
# Solution.==>

print("Welcome to Counting Print Program.")
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
while start_Num <= end_Num:
    print(start_Num)
    start_Num +=1
end = input("Thanks for using the Program. Press Enter to Exit the Program.")
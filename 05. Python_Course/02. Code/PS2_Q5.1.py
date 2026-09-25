# Q 5.1 Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break ).
# Solution ==>

print("Welcome to Pyton Print Program.")
while True:
    try:
        num1 = int(input("Please Enter your number which you want to Find : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")

i = 0
while i < 1000000000000000000000000000000000:
    print(i)
    if i == num1:
        break
    else:
        i +=1
print("Thanks for Using The Program.")
end = input("press Enter to Exit.")



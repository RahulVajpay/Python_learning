# Q 3.2 Print the multiplication table of a number (entered by user).
# Solution.==>

print("Welcome to Multiplication Table Print Program.")
while True:
    try:
        num1 = int(input("Please Enter Which Number Table You Want to Print. :"))
        if num1 > 0:
            break
        else:
            print("Please enter a Positive Number.")
    except ValueError:
        print("Please enter a Valid Number Not a String.")
i = 1
for i in range (1,11):
    print(f"{num1}\tx\t{i}\t=\t{num1*i}")
    i +=1
print(f"We have Successfully Printed the Multiplication table of {num1}.")
end = input("Press Enter to Exit The Program....")
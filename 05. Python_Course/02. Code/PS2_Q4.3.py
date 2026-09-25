# Q 4.3 Use a while loop to reverse a given number (e.g., 123 → 321).
# Solution.==>

print("Welcome to Number Reverse Program.")
while True:
    try:
        num1 = int(input("Please Enter your Number to Reverse. : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")
strnum = str(abs(num1))
str_len = len(strnum)
rev_num  = ""
i = 0
while i < str_len:
    rev_num = strnum[i] + rev_num
    i +=1
if num1 > 0:
    print(f"Reverse Number of your Number {num1} is {rev_num}")
else:
    print(f"Reverse Number of your Number {num1} is -{rev_num}")
end = input("Thanks for Using the Program...\nPress Enter to Exit the Program.")
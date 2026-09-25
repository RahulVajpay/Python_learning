# 27. Reverse a number
# Solution ==>

def greet ():
    print("Welcome to Palindrome Number Check Program.")

def _Palindrome(num):
    absnum = abs(num)
    revnum = 0
    if num > 0:
        sign = 1
    else:
        sign = -1
    while absnum > 0:
       revnum = revnum * 10 + (absnum%10)
       absnum //=10
    if num == revnum*sign:   
       print(f"You Have Entered a Palindrome Number.")
    elif num != revnum*sign:   
       print(f"Sorry!! Your Number is Not Palindrome.")


greet()
while True:
    try:
        num1 = int(input("Please Enter a Number which you want to Check. : "))
        if num1 == 0:
            print("Number Should not be Zero.")
        else:
            break    
    except ValueError:
        print("Please Enter a Valid Number.")

_Palindrome(num1)
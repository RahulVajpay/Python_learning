# Write a recursive function factorial(n) that returns the factorial of a number.
# Soltion ==>

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print("Welcome to Factorial Calculation Program.")
while True:
    try:
        _num = int(input("Please Enter a Number Which Factorial you want to Calculate. : ".title()))
        if _num <=0:
            print("Please Enter a Positive a Non Zero Number.".title())
        else:
            break
    except ValueError:
        print("Please Enter a Valid Number.".title())
print(f"{_num}! = {factorial(_num)} \nThe Total Number of Charachter in this is {len(str(factorial(_num)))}")
end = input("Press Enter to Exit the Program..".title())

     

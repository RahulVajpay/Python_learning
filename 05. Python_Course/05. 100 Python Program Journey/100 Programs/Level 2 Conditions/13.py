# 13. Largest of Two Numbers
# Solution ==>

print("Welcome to Largest of Two Numbers Identifier Program.")

while True:
    try:
        num1 = float(input("Please Enter your First  Number : "))
        while True:
            try:
                num2 = float(input("Please Enter your Second Number : "))
                break        
            except ValueError:  
                print("Please Enter a Number.")         
        break
    except ValueError:  
        print("Please Enter a Number.")

if num1 > num2:
    print(f"Your First Number {num1} is Graeter than your Second Number {num2} by {num1-num2}")
elif num1 < num2:
    print(f"Your Second Number {num2} is Graeter than your Frost Number {num1} by {num2-num1}")
else:
    print("Both Numbers You Entered is Equal.")        
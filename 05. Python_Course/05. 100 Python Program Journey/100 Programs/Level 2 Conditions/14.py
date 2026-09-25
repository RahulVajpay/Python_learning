# 14. Largest of Three Numbers
# Solution ==>

print("Welcome to Largest of Three Numbers Identifier Program.")

while True:
    try:
        num1 = float(input("Please Enter your First  Number : "))
        while True:
            try:
                num2 = float(input("Please Enter your Second Number : "))
                while True:
                    try:
                        num3 = float(input("Please Enter your Third Number   : "))
                        break
                    except ValueError:
                        print("Please Enter a Number.")
                break        
            except ValueError:  
                print("Please Enter a Number.")         
        break
    except ValueError:  
        print("Please Enter a Number.")

if num1 > num2 and num1 > num3 and num2!=num3:
    print(f"Your Largest Number is {num1}")

elif num2 > num1 and num2 > num3 and num1!=num3:
    print(f"Your Largest Number is {num2}")

elif num3 > num1 and num3 > num2 and num1!=num2:
    print(f"Your Largest Number is {num3}")

elif num1 == num2 and num1 > num3 :
    print(f"Your Largest Number is {num1}")

elif num1 == num2 and num1 < num3 :
    print(f"Your Largest Number is {num3}")

elif num1 == num3 and num1 > num2 :
    print(f"Your Largest Number is {num1}")

elif num1 == num3 and num1 < num2 :
    print(f"Your Largest Number is {num2}")

elif num2 == num3 and num2 > num1 :
    print(f"Your Largest Number is {num2}")

elif num2 == num3 and num2 < num1 :
    print(f"Your Largest Number is {num1}")
else:
    print("All Numbers You Entered are Equal.")  
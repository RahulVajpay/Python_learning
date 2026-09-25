# 5. Multiply two numbers
# Solution ==>


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
print(f"{num1} x {num2} : {num1 * num2}")        
        
        
        
# Q 5.1 Print numbers from 1 to 10, skipping the number 5 (use continue ).
# Solution ==>

print("Welcome to Pyton Print Program.")
while True:
    try:
        num1 = int(input("Please Enter your number which you want to Skip : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")

i = 0
while i <= 100:    
    if i == num1:
        i +=1 
        continue      
    else:
        print(i)
        i +=1
print(f"Thanks for Using The Program. {num1} is Skip.")
end = input("press Enter to Exit.")



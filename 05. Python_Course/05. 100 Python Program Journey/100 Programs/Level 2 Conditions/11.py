# 11. Even or Odd Number
# Solution ==>

print("Hi Welcome to Even Odd Checker Program.!!")
while True:
    try:
        num = int(input("Please Enter a Your Number. "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")

if num % 2 ==0:
    print(f"{num} is a Even Number")
else :
    print(f"{num} is a Odd Number")    

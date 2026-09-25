# 20. Check Divisibility by 5 and 11
# Solution ==>

while True:
    try:
        num = int(input("Please Enter your Number. : "))
        break
    except ValueError:
        print("Please Enter a Valid Number.")

if num%5 == 0 and num%11 ==0:
    print(f"{num} is Divisible by Both 5 and 11.")
else:
    print(f"{num} is not Divisible by Both 5 and 11.")
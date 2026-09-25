# 23. Sum of first N numbers.
# Solution==>

print("Welcome to Sum of N number print Program.")
while True:
    try:
        num = int(input("Please Enter the Number upto which you want Sum of Num : "))
        if num <= 0:
            print("Please Enter a Valid Positive integer.")
        else:    
            break
    except ValueError:
        print("Please Enter a Valid Integer.")

_sum = 0
for i in range(1, num + 1):
    _sum += i

print(f"Sum of Upto {num} is {_sum}")    

# 37. Reverse Triangle
# Solution ==>

def greet ():
    print("Welcome to Reverse Triangle Pattern printing program.")


def print_reverse_triangle(num):
    for i in range(1, num+1):
        print('*'*(num+1-i))


greet()
while True:
    try:
        num = int(input("Please Enter the Height of the Triangle : "))
        if num <=1:
            print("Please Enter a Positive Number Greater than 1.")
        else:
            break    
    except ValueError :
        print("Please Enter a Valid Number")       

print_reverse_triangle(num)

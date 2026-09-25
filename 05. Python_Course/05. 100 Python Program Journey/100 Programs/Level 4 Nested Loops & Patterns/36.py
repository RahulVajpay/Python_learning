# 36. Star Triangle
# Solution ==>

def greet ():
    print("Welcome to Triangle Pattern printing program.")


def print_triangle(num):
    for i in range(1, num+1):
        print('*'*i)


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

print_triangle(num)

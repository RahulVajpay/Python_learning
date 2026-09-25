# 38. Pyramid Pattern
# Solution ==>

def greet ():
    print("Welcome to Pyramid Pattern printing program.")


def print_pyramid(num):
    for i in range(1, num+1):
        print(' '*((num)-i)+"*"*(2*i-1))


greet()
while True:
    try:
        num = int(input("Please Enter the Height of the Pyramid : "))
        if num <=1:
            print("Please Enter a Positive Number Greater than 1.")
        else:
            break    
    except ValueError :
        print("Please Enter a Valid Number")       

print_pyramid(num)


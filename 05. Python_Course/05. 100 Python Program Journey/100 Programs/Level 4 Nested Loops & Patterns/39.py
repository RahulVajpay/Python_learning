# 39. Inverted Pyramid
# Solution ==>


def greet ():
    print("Welcome to inverted Pyramid Pattern printing program.")


def print_inverted_pyramid(num):
    for i in range(1, num+1):
        print(' '*(i-1)+"*"*(2*(num-i)+1))


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
print_inverted_pyramid(num)


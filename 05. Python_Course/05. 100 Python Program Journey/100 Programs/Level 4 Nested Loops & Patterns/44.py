# 44. Hollow Square Pattern
# Solution ==>

def greet ():
    print("Welcome to Hollow Square Pattern printing program.")


def hollow_square(num):
    print('* '*num)
    for i in range(1, num-1):
        print('* ' + '  '*(num-2) + '*')
    print('* '*num) 

greet()
while True:
    try:
        num = int(input("Please Enter the Size of the Square : "))
        if num <=1:
            print("Please Enter a Positive Number Greater than 1.")
        else:
            break    
    except ValueError :
        print("Please Enter a Valid Number")   

hollow_square(num)  
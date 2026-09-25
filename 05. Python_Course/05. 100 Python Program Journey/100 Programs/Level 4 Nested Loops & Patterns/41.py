# 41. Floyd's Triangle
# Solution ==>

def greet ():
    print("Welcome to Floyd's Triangle printing program.")


def print_floyds_triangle(num):
    count = 1
    for i in range(1, num+1):        
        j = 1 
        while j <= i:
            print(count, end = " ")
            j +=1
            count +=1
        print()           


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

print_floyds_triangle(num)






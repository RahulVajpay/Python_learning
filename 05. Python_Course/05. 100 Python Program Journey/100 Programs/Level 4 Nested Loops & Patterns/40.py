# 40. Number Triangle
# Solution ==>



def greet ():
    print("Welcome to Number Triangle printing program.")


def print_number_triangle(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end = " ")
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

print_number_triangle(num)






# 43. Diamond Pattern
# Solution

def greet ():
    print("Welcome to Diamond Pattern printing program.")


def print_diamond(num):
    if num %2 == 0:
       height = int(num/2)
       for i in range(1, height+1):
           print(' '*((height)-i) + "*"*(2*i-1))
       for i in range(1, height+1):
           print(' '*(i-1) + "*"*(2*(height-i)+1)) 
    else :
        height = int(num//2 + 1)
        for i in range(1, height+1):
            print(' '*((height)-i) + "*"*(2*i-1))
        for i in range(2, height+1):
            print(' '*(i-1) + "*"*(2*(height-i)+1))

      
greet()
while True:
    try:
        num = int(input("Please Enter the Height of the Diamond : "))
        if num <=1:
            print("Please Enter a Positive Number Greater than 1.")
        else:
            break    
    except ValueError :
        print("Please Enter a Valid Number")       

print_diamond(num)
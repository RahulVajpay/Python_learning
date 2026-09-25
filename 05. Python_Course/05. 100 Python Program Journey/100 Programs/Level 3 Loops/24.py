# 24. Multiplication Table
# Solution ==>

def greet():
    print("Welcome to Multipication table print progaram.")

def _table(num):
    for i in range(1, 11):
        print(f"{num}\tX\t{i}\t= {num*i}")

greet()
while True:
    try:
        num1 = int(input("Please Enter the Number which table you want to print.: "))
        if num1 <=0 :
            print("Please Enter a Valid Positive integer.")
        else:
            break    
    except ValueError:
        print("Please Enter a valid Number.")
_table(num1)



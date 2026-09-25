# 45. Multiplication Table Matrix
# Solution ==>

def greet():
    print("Welcome to the Multiplication Table Printing Program.")

def multiplication_matrix(row, column):
    for i in range(1, row + 1):
        for j in range (1, column + 1):
            print(f'{i*j}\t',end = " ")
        print()    

greet()
while True:
    try:
        row = int(input("Please Enter the Numbers of Rows: "))
        if row <=1:
            print("Please Enter a Positive Number Greater than 1.")
        else:
            break    
    except ValueError :
        print("Please Enter a Valid Number")
while True:
    try:
        column = int(input("Please Enter the Numbers of Columns: "))
        if column <=1:
            print("Please Enter a Positive Number Greater than 1.")
        else:
            break    
    except ValueError :
        print("Please Enter a Valid Number")          

multiplication_matrix(row,column)
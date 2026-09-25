# 30. Fibonacci Series
# Solution ==>


import sys


def greet ():
    print("Welcome to Fibonacci Number Find Program.")

def Fibonacci(num):
    fib1 = 0
    fib2 = 1
    if num == 1:
        return fib1
    elif num == 2:
        return fib2
    else:
     i = 2
     Fibo = 0
     while i < num:
         Fibo = fib1 + fib2
         fib1 = fib2
         fib2 = Fibo
         i+=1
     return Fibo

greet()
while True:
    try:
        num1 = int(input("Please Enter your Index Number : "))
        if num1 <= 0:
            print("Number Should not be Zero or Negative.")
        else:
            break    
    except ValueError:
        print("Please Enter a Valid Number.")

print(f"Your Fibonacci Number is {Fibonacci(num1)}")
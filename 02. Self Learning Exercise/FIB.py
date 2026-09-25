def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-2) + fib(n-1)

fibn = int(input("Please Enter which fibbnocci number you want. : "))
print(f"The {fibn}th Fibonacci number is: {fib(fibn)}") 



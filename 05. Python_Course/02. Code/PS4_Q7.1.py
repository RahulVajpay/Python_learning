# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
# Solution==>

def Fibonacci(n):
    if n == 0 or n ==1:
        return n 
    else :
        return Fibonacci(n-2) + Fibonacci(n-1)

num = int(input("Which Fibonacci number you want to find ? : "))
print(f"The {num}th Fibonacci Number is : {Fibonacci(num)} ")
end = input("Thanks for using the program. Press Enter to Exit...")

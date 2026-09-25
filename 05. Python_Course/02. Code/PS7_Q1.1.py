# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".
# Solution ==>

def logger (func):
    def wrapper ():
        print("Function is being called...")
        func()
        print("Function is Executed....")
    return wrapper

def say_hello():
    print("Hello!")

f = logger(say_hello)   # First Way to Use Decorator.
f()

@logger                 # Second Way to Use Decorator.
def print_hello():
    print("Hello!")

print_hello()    
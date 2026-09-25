# Write a function safe_divide(a, b) that returns the result of a / b , but returns "Cannot divide by zero" if b is 0 .
# Solution ==>

def divide(a , b):
    if b ==0:
        return "You Cannot divide by zero"
    else:
        return a/b
    
print(divide(10,0))
print(divide(10,2))

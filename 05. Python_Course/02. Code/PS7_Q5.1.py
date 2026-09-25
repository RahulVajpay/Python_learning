# Write a program that asks the user to enter a number and handles:
# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
# Create a custom exception NegativeNumberError and raise it when the user
# enters a negative number.
# Solution ==>

while True:
    try:
        a = int("Please Enter Your First NUmber  : ")
        b = int("Please Enter your Second Number : ")
        sum = a + b
        Product = a * b
        diff = a - b
        divi = a/b
        if b == 0:
    except ZeroDivisionError:

    except ValueError:
        print("Please Enter a Number.")
        if b == 0:
         except ZeroDivisionError:



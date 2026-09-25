# Write a function square(num) that returns the square of a given number. Test it with different numbers.
# Soltion ==>

def square(num):
    c = num * num
    return c
print("Welcome to the Square of a Number Finding Program...".title())
num1 = int(input("Please Enter your number which square you want to Calculate. : ".title()))
print(f"The Square of {num1} = {square(num1)}".title())
end = input("Press Enter to Exit the Program..".title())
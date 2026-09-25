# Write a function multiply(a, b) that has a proper docstring explaining what
# it does. Then use help(multiply) to display the docstring.
# Solution==>

def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

print(multiply.__doc__)  # Display the docstring
print("-----------------------------------------------------")
help(multiply)           # Alternatively, display the docstring with help()
#Problem Statement:

"""A commerce operations engineer must prepare a small checkout-rule script for a cart total and 
membership value. Build a Python script that converts the cart total from text to a number, 
displays the converted total, and prints whether free delivery and discount eligibility are 
True or False.
"""

#Constraints & Requirements:

"""
Use the shown cart_total and is_prime_member values as the inputs.
Convert the cart total with float() before numeric comparisons.
Free delivery requires a total of at least 1000 and membership equal to "yes".
Discount eligibility requires a total of at least 500 or membership equal to "yes".
Use if/else blocks with colons and consistent indentation.
"""
#Inlined Sample Data & Inputs:

"""
Sample input shown to the student (verbatim): cart_total = "1150" and is_prime_member = "yes"
Expected output for that sample: display Cart total: 1150.0, 
then Free delivery: True, then Discount eligible: True
"""

# Solution:
cart_total = "1150"
is_prime_member = "yes"
discount_eligible = False
free_delivery = False

# Convert cart_total to a float
cart_total_float = float(cart_total)
if cart_total_float >= 500 and cart_total_float < 1000 and is_prime_member == "yes":
    discount_eligible = True
elif cart_total_float >= 1000 and is_prime_member == "yes":
    free_delivery = True
    discount_eligible = True
else:
    discount_eligible = False
    free_delivery = False    

print(f"Cart total: {cart_total_float}")
print(f"Free delivery: {free_delivery}")
print(f"Discount eligible: {discount_eligible}")


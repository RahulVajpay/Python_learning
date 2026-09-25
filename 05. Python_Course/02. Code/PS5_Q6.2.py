# Given a dictionary of products and their prices, find the product with the highest price.
# Solution ==>

product_dict = {"Python Course" : 5000 , "C# Course" : 10000, "AI & ML Course" : 50000, "All Course Bundle" : 100000}

# Method 1

Higher_Course = ""
Higher_Course_price = 0

for item in product_dict:
    if product_dict[item] > Higher_Course_price :
        Higher_Course_price = product_dict[item]
        Higher_Course = item
print(f"This output is from Method 1. The Highest Price of the Course \"{Higher_Course}\" is {Higher_Course_price}")

# Method 2

Higher_Course = ""
Higher_Course_price = 0

for item in product_dict.keys():
    if product_dict[item] > Higher_Course_price :
        Higher_Course_price = product_dict[item]
        Higher_Course = item
print(f"This output is from Method 2. The Highest Price of the Course \"{Higher_Course}\" is {Higher_Course_price}")


# Method 3
Higher_Course = ""
Higher_Course_price = 0

for item , value in product_dict.items():
    if value > Higher_Course_price:
        Higher_Course_price = value
        Higher_Course = item
print(f"This output is from Method 3. The Highest Price of the Course \"{Higher_Course}\" is {Higher_Course_price}")
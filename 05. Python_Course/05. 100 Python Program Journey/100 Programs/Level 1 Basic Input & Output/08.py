# 8. Find cube of a number
# # Solution ==>

while True:
    try:
        num1 = float(input("Please Enter your Number which Cube you want to Find: "))
        break
    except ValueError:
        print("Please Enter a Number.")
print(f"Cube({num1}) = {num1**3}")            
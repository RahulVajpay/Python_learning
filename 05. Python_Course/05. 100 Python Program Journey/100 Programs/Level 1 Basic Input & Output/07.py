# 7. Find square of a number
# # Solution ==>

while True:
    try:
        num1 = float(input("Please Enter your Number which Sqare you want to Find: "))
        break
    except ValueError:
        print("Please Enter a Number.")
print(f"Square({num1}) = {num1**2}")            
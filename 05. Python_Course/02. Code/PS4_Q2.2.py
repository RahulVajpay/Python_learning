# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# 1. Both length and width
# 2. Only length (use default width)
# Solution ==>

def rec_area(length, width = 10):
    area = length * width
    return area

print("Welcome to the Program to Calculte the Area of Rectangle.".title())
while True:
    try:
        _length = float(input("Please Enter the Length of Rectangle. : ".title()))
        if _length <=0:
            print("Please Enter a Positive or Non Zero Length.".title())
        else:
            break
    except ValueError:
        print("Please Enter a Valid Number..".title())
while True:
    try:
        _Width = float(input("Please Enter the Width  of Rectangle. : ".title()))
        if _Width <=0:
            print("Please Enter a Positive or Non Zero Length.".title())
        else:
            break
    except ValueError:
        print("Please Enter a Valid Number..".title())
print(f"The Area of Rectangle of Side L: {_length} and W: {_Width} = {rec_area(_length,_Width)} ")
end = print("thanks for using the Program".title())
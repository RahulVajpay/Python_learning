# 18. Grade Calculator
# Solution ==>

print("Welcome to Grade Calculator Program..")

def Grade(Percentage):
    if Percentage > 90:
        return "A+"
    elif Percentage >= 80 and Percentage <= 90:
        return "A"
    elif Percentage >= 70 and Percentage < 80:
        return "B+"
    elif Percentage >= 60 and Percentage < 70:
        return "B"
    elif Percentage >= 50 and Percentage < 60:
        return "C+"
    elif Percentage >= 40 and Percentage < 50:
        return "C"
    elif Percentage < 40 and Percentage >= 33:
        return "D"
    else:
        return "Fail"

while True:
    try:
        _percentage = float(input("Please Enter your Percentage : "))
        break
    except ValueError:
        print("Please Enter a Valid Marks.")


if Grade(_percentage) != "Fail":
    print(f"Your Garde is {Grade(_percentage)}.")
else:
    print(f"Sorry You Are {Grade(_percentage)}.")    

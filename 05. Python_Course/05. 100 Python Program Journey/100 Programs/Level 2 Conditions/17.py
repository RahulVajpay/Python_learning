# 17. Check Leap Year
# Solution ==>

while True:
    try:
        _year = int(input("Please Enter year which you want to Check is a Leap year : "))
        break
    except ValueError:
        print("Please Enter a Valid Year...")

if _year % 400 == 0:
    print(f"Year {_year} is a Leap Year.")
elif _year % 100 == 0:
    print(f"Year {_year} is not a Leap Year.")
elif _year % 4 == 0:
    print(f"Year {_year} is a Leap Year.")    
else:
    print(f"Year {_year} is not a Leap Year.")    

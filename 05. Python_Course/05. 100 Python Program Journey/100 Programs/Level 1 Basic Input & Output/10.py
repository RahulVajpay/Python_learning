# 10. Calculate area of circle.
# Solution ==>

from math import pi as PI

while True:
    try:
        radius = float(input("Please Enter your Circle's Radius : "))
        break
    except ValueError:  
        print("Please Enter a Number.")       
print(f'''
Circle's Perimeter : {2*(radius * PI)}
Circle's Area      : {PI * radius**2}
      ''') 
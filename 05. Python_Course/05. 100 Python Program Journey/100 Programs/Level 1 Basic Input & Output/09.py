# 9. Calculate area of rectangle.
# Solution ==>

while True:
    try:
        length = float(input("Please Enter your Rectangle Length : "))
        while True:
            try:
                width = float(input("Please Enter your Rectangle Width  : "))
                break        
            except ValueError:  
                print("Please Enter a Number.")         
        break
    except ValueError:  
        print("Please Enter a Number.")       
print(f'''
Rectangle's Perimeter : {2*(length + width)}
Rectangle's Area      : {length * width}
      ''') 
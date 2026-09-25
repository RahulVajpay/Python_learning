# Q 3.4 Print numbers from 1 to 10 using a for loop.
# Solution.==>

print("Welcome to Right Angle Triangle Print Program.")
while True:
    try:
        Tri_Base = int(input("Please Enter the Base Dimension of Your Triangle. :"))
        if Tri_Base<=0:
            print("Please provide the Positive Dimension.")
        else:
            break
    except ValueError:
        print("Please Enter a Number.")
while True:
    try:
        Tri_Height = int(input("Please Enter the Base Dimension of Your Triangle. :"))
        if Tri_Height<=0:
            print("Please provide the Positive Dimension.")
        else:
            break
    except ValueError:
        print("Please Enter a Number.")

Tri_base = Tri_Base
Tri_height = Tri_Height
for row in range(1, (Tri_Height+1)):
# Formula to Calculate the Stars in each row Used.
    stars = (Tri_Base * row)//Tri_Height
    print("*"*stars)
    row +=1
print('Congeatulations!! You have successfully Print your Desired Traingle.')
print(f"The Height and Base of Your Triangle is {Tri_height} and {Tri_base} and Area is {0.5*Tri_base*Tri_base}")
end = input("Press Enter to Exit the Program.")

    
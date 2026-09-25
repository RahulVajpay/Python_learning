# Write a recursive function sum_of_digit(n) that returns the sum of all digits of a given number.
# Solution ==>


def sum_of_digit(n):
    if n ==0 :
        return 0
    else :
        return n%10 + sum_of_digit(n//10)


    
print("Welcome to Sum of Digit of a number Calculation Program.".title())
while True:
    try:
        _num = int(input("Please Enter a Number which digit sum you want to Calculate. : ".title()))
        if _num <=0:
            print("Please Enter a Positive a Non Zero Number.".title())
        else:
            break
    except ValueError:
        print("Please Enter a Valid Number.".title())
print(f"Sum of All Digit of {_num} = {sum_of_digit(_num)} \nThe Total Number of Charachter in this is {len(str(sum_of_digit(_num)))}")
end = input("Press Enter to Exit the Program..".title())

     

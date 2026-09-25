# Q 2.1 Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case 
# Solution ==>

print("Welcome to Pick Program.")
while True:
    try:
        num1 = int(input("Please Enter your Number to Check. :"))
        if 1<=num1<=7:
            break
        else:
            print("Please Enter a Number Between 1 to 7")
    except ValueError:
        print("Please Enter a Valid Number to Check.")
match num1 :
    case 1:
        print("its Monday.")
    case 2:
        print("its Tuesday.")
    case 3:
        print("its Wednesday.")
    case 4:
        print("its Thusrsday.")
    case 5:
        print("its Friday.")
    case 6:
        print("its Saturday.")
    case 7:
         print("its Sunday.")
    case _:
         print("Wow You have full Week Holiday.")
end = input("Press Enter to Exit the Program...")

print('\t\t "Welcome to Odd Even Checker!" \t\t')
try:
    number = int(input("Enter Your number: "))
    if number % 2 == 0:
# This is First Way to print String and Intreger together Note if you are using + insted of , 
# then you have to convert number into string using str() function otherwise it will give you 
# error because you can't concatenate string and integer together.
        print("\n This", number , "is an Even Number.")                   
    else:
# This is Second Way to print String and Intreger together
        print(f"\n This {number} is an Odd Number.")                       
    print("\n\t\tThank You For Using The Odd Even Checker! \t\t")
except ValueError:
    print("\n\t\tInvalid input! Please enter a valid integer. \t\t")
end = input("Press Enter to exit the program.")
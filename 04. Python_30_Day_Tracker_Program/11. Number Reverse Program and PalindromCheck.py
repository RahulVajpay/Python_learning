print('\t\t"Welcome to Number Reverse Program"')
# This loop will continue until the user enters a valid number and the program executes successfully.
while True:                
# The try block is used to catch any ValueError exceptions that may occur when the user enters an invalid input 
# (e.g., a non-integer value). If an exception occurs, the program will print an error message and prompt the user to enter a valid number again.
    try:                    
        num1 = int(input("Please Enter a Number Which You want to Reverse :"))
        original_num = num1
# The if statement checks if the absolute value of the input number has less than 2 digits. If it does, it prompts the user to enter a number with 
# at least two digits and continues the loop to ask for input again. abs Function is used to handle negative numbers, 
# ensuring that the digit count is based on the magnitude of the number rather than its sign.
        if len(str(abs(num1)))<2:
                print('Please Enter Atleast Two Digit Number.')
# continue statement is used to skip the rest of the code in the current iteration of the loop and start the next iteration, 
# allowing the user to enter a new number without executing the reversal logic for an invalid input.
                continue
        else:
             if num1 < 0:
                  sign = -1
             else:                   
                  sign = 1
             num1 = abs(num1)
             rev01 = 0
             while num1 > 0:
                  digit = num1 % 10
                  rev01 = (rev01 * 10 + digit)
                  num1 = num1//10
        print(f'Reverse of  {original_num} is {rev01 * sign}')
# A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome because 
# it reads the same backward and forward, while 123 is not a palindrome because it reads differently when reversed (321). 
# The code checks if the reversed number (rev01 * sign) is equal to the original number (original_num) to determine if it is a palindrome or not.
        if rev01 * sign == original_num:
            print(f'{original_num} is a Palindrome Number.')  
        else:
            print(f'{original_num} is not a Palindrome Number.')
        break               
    except ValueError:
        print('Please Enter a valid Number.')
end = input('Please Press enter to exit the Program')
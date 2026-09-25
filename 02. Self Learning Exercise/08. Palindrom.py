print('\t\tWelcome to Palindrome Number Find Program')
#-----First Number Input.----------
while True:
    try:
        num1 = int(input('Please Enter your First Number of Series : '))
        if len(str(abs(num1)))<2:
            print('Please Enter a two digit Number.')
            continue
        break           
    except ValueError:
        print('Please Enter a Valid Number.')
#-----Second Number Input.----------
while True:
    try:
        num2 = int(input('Please Enter your Second Number of Series : '))
        if num2<=num1:
            print('Please Enter number greater than your first Number.')
            continue
        break           
    except ValueError:
        print('Please Enter a Valid Number.')
print(f'You want to Check Palindrome between {num1} and {num2}')
#---Main Logic---------
i = num1
count = 0
palindrome_list = []
while i <= num2:
    num = i
    temp = abs(num)
    reversenum = 0
    if num < 0:
        sign = -1
    else :
        sign = 1
    while temp > 0:
        digit = temp%10
        reversenum = reversenum * 10 + digit
        temp = temp//10
    if(num != (reversenum * sign)):
        print(f'Reverse of {num} is {reversenum * sign} and This is not a Palindrome Number')
    else:
        print(f'Reverse of {num} is {reversenum * sign} and This is a Palindrome Number')
        palindrome_list.append(reversenum)
        count +=1
    i+=1
print((f'Total Number of Palindrome Number between {num1} and {num2} is {count}. Please find them below'))
print(palindrome_list)
end = input('Press Enter to Exit the Program.')

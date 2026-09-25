print('\t\t Welcome to the Reverse Counting Calculator! \t\t')
try:
    Number = int(input('Please enter a number to start reverse counting: '))
    i = Number
    if i < 0:
        print('Please enter a positive number!')
    else:    
        while i>=0:
         print(i)
         i -= 1    
except ValueError:
    print('Please enter a valid number!')
end = input('Press Enter to exit the program...')
print('\t\t Welcome to the Sum of N-Numbers Calculator! \t\t')
try:
    num = int(input('Enter a positive integer: '))
    i = 1
    sum = 0
    if num < 0:
        print('Invalid input! Please enter a positive integer.')
    else:    
        while i <= num:
            sum += i
            i += 1
        print(f'The sum of the first {num} natural numbers is: {sum}')
except ValueError:
    print('Invalid input! Please enter a positive integer.')
print('Thank you for using the Sum of N-Numbers Calculator!')


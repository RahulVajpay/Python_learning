print('\t\t Welcome to the Sum of N Number Program!!')
while True:
    try:
        n = int(input('Enter the number of terms you want to add: '))
        if n < 0:
            print('Please enter a non-negative integer.')
            continue
        else:
            i = 1
            Total = 0
            while i <=n:
                Total += i
                i += 1
            print(f'The sum of the first {n} natural numbers is: {Total}')
        break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    
end = input('Press Enter to exit the program...')

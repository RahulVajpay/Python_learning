print('\t\t Welcome to the Print Numbers from 0 to N Calculator! \t\t')
try:
    number = int(input('Please enter a positive integer (N): '))
    i = 0
    while i <= number:
        print(i)
        i += 1
except ValueError:
    print('Please enter a valid positive integer.')
end = input('Press Enter to exit the program.')
    
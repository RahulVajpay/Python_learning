print('\t\t Welcome to the odd Number Print Program \t\t')
try :
    Number = int(input('Enter the positive number : '))
    i = 1
    if Number < 0 :
        print('Please enter a positive number')
    else :
        while i <= Number :
            print(i)
            i += 2
except ValueError :
    print('Please enter a valid number')    
print('\t\t "Welcome to Multiplication Table Print Program !!"')
while True:
    try:
        num1 = int(input('Please Enter the number Which Table you Want to Print: '))
        if num1 < 0:
            print('Please Enter a Non-Negative Number.')
            continue
        else:
            i= 1
            table = 1
            while i <=10:
                table = (i)*num1
                print(f'{num1} x {i}\t= {table}')
                i += 1                    
        break
    except ValueError:
         print('You have entered a wrong Number.')
end = input('Please Press enter to exit the Program')



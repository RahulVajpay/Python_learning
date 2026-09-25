print('Welcome to the Number Checking Program!')
try:
    number = int(input('Please enter a number: '))
    if number > 0:
        print(f'The number {number} is positive.')
    elif number < 0:
        print(f'The number {number} is negative.')
    else:        
        print('The number is zero.')    
except ValueError:
    print('Invalid input. Please enter a valid number.')
end = input('Press Enter to exit the program.')
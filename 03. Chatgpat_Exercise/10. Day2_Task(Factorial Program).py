print('\t\t Welcome to Facorial Program! \t\t')
try:
    factNum = int(input('Please Enter a Number Which Factorial You Want : '))
    i = int(1)
    fact = int(1)
    while i <= factNum:
        fact *= i
        i += 1
    print(f'Factorial of {factNum} : = {fact} and Len of Factorial is : {len(str(fact))}')
except ValueError :
    print('Invalid Number Enter. Please Enter a valid number.')
end = (input('Press Enter to Exit'))

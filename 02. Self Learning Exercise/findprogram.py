print('Welcome to Find Program.')
while True:
    try:
        num = int(input('Enter a number: '))
        break
    except ValueError:
        print('Please Enter a Valid Number.')
strnum = str(num)
length = len(strnum)
Counter = 0
i = 0
j = 2
while i < length-1:
    if strnum[i:j] == '10':  
        Counter += 1
    i += 1
    j += 1
print('The Number of Times 10 Occurs in the Given Number is:', Counter)

  



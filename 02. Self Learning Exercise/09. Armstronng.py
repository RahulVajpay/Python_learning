print('Welcome to Armstrong Number Check Program!!')
while True:
    try:        
        num1 = int(input('Please Enter Your Number : '))
        if num1 < 0:
            print('Please Enter a Positive Number.')
            continue
        else:
            break
    except ValueError:
        print('Please Enter a valid Number.')
i = 0
lt = len(str(num1))
str1 = str(num1)
total = 0
while i < lt :
      total = total + int(str1[i])**lt
      i +=1
if total == num1:
    print('You have Enter a Armstrong Number.')
else: 
    print('This is Not a Armstrong Number.')
end = print('Press Enter to Exit the program.')
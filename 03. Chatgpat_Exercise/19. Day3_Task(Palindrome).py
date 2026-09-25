print('\t\t"WELCOME TO NUMBER OF PALINDROME NUMBER FIND PROGRAM!!"')
while True:
    try:
        start_No = int(input('Please Enter your Series Start Number. : '))       
        if len(str(abs(start_No)))< 2:
            print('Please enter a atleast Two digit Number')
            continue
        else :
            while True:
                try:
                    end_No = int(input('Please Enter your Series End Number. : '))
                    if ((int(end_No) > int(start_No))== False):
                        print('End number must be greater than start number')
                        continue
                    break
                except ValueError:
                    print('Please Enter a Valid Number.')
        i = start_No
        count = 0
        while i <= end_No:
            num = i
            temp = num
            rev = 0
            while temp > 0:
                digit = temp%10
                rev = (rev *10  + digit)
                temp = temp // 10
            if num != rev:
                print(f'Reverse of {num} is {rev} and This is not a Palindrome Number')
            else:
                print(f'Reverse of {num} is {rev} and This is a Palindrome Number')
            if num == rev:
                count += 1            
            i += 1
        print(f'Total Palindrom Number between {start_No} and {end_No} is {count}')
        break               
    except ValueError:
        print('Please Enter a Valid Number.')    
end = input ('Press Enter to exit the Program.')
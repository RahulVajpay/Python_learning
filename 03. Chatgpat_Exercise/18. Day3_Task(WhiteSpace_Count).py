print('\t\t"Welcome to White Speace Coount Program!!"')
string1 = input('Please input your string to Check the White Space. : ')
i = 0
j = 0
while i<=len(string1) - 1:
    print(string1[i])
    if str.isspace(string1[i]):
        j += 1
    i +=1
print('Number of white spaces:', j)
end = input('Press Enter to Exit.')

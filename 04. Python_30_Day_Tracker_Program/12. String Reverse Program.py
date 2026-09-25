print('\t\t"Welcome to String Reverse Program !"')
string1 =(input('Please Enter a String to Reverse. : '))
# i is the index of the last character in the string therefore we use len(string1)-1 to get the index of the last character
i = len(string1)-1
# we will use a while loop to iterate through the string in reverse order and concatenate the characters to rev_str
# initially required a Empty String variable to store the reversed string and we will concatenate the characters to it in each iteration of the loop
rev_str = ""                    
while i >= 0:
    rev_str = rev_str + string1[i]
    i -=1
print(rev_str)

Name = "Rahul Vajpayee"
Mobile = int(7982362429)

# We Can Combine String With Other Data Types Using Comma(,) In Print Function. Find Example Below
print("Hello Mr.", Name + ", your mobile number is", Mobile)

# Below Is the example of Multiple Line Comment in Python.
# Any thing in between the triple Single or Double quotes is considered as comment and will not be executed by the Python Interpreter. Find Example Below
"""
We Can Combine String With Other Data Types Using Plus(+) In Print Function But It Will Give Error 
If We Don't Convert The Other Data Type To String AND it will not add White Space by Self. Find Example Below
"""
print("Hello Mr. " + Name + ", your mobile number is " + str(Mobile))

# Find example below to determine the length of the string using len() function.
# And we can also find the length of the string by converting other data type to string using str() function. Find Example Below  
print("The length of the string is:", len(Name))
print("The length of the string is:", len(str(Mobile)))

# Find example below to Access the characters of the string using indexing. Indexing starts from 0 in Python. Find Example Below
print("The first character of the string is:", Name[0])
print("The second character of the string is:", Name[1])
print("The third character of the string is:", Name[2])
print("The fourth character of the string is:", Name[3])
print("The fifth character of the string is:", Name[4])
print("The sixth character of the string is:", Name[5])
print("The seventh character of the string is:", Name[6])
print("The eighth character of the string is:", Name[7])
print("The ninth character of the string is:", Name[8])
print("The tenth character of the string is:", Name[9]) 
print("The eleventh character of the string is:", Name[10])
print("The twelfth character of the string is:", Name[11])
print("The thirteenth character of the string is:", Name[12])
print("The fourteenth character of the string is:", Name[13])

'''
Find example below to Access the characters of the string using slicing. 
Slicing is used to access a range of characters in a string. Slicing is done by using the colon(:) operator. The syntax for slicing is string[start:end].
The start index is inclusive and the end index is exclusive. Means the character at the start index will be included in the result but the character 
at the end index will not be included in the result. Find Example Below
'''
print("The First Five Characters Of The String Are:", Name[0:5])
print("The Last Five Characters Of The String Are:", Name[6:14])
print("The First Five Characters Of The String Are:", Name[:5])
print("The Last Five Characters Of The String Are:", Name[6:])

#Find example below to Access the characters of the string using negative indexing. Negative indexing starts from -1 in Python. Find Example Below
# For Negative Slicing it Will Print The Characters From The End Of The String or Character at this Location len(String) - index. Find Example Below
print("The Last Character Of The String Is:", Name[:-1])
print("The Last Character Of The String Is:", Name[-3])

'''
 Find the Example Below for Multiple Line String in Python. Multiple Line String is a string that is defined in multiple lines. It is defined by 
 using triple single or double quotes. Find Example Below
'''

Multiple_Line_String = """This is a multiple line string in Python.
It is defined by using triple double quotes."""
print(Multiple_Line_String)

# Find the example of Escaping Characters in Python. Escaping Characters are used to print special characters in a string.
#  It is done by using the backslash(\) before the special character. Find Example Below  

Escaped_String1 = "This is a string with escaped characters: \nLine 1\nLine 2"    # \n is used to print a new line in the string.
Escaped_String2 = 'This is a string with escaped characters: \tLine 1\tLine 2'    # \t is used to print a tab in the string.
Escaped_String3 = " Hello Mr. Rahul Vajpayee, \"Welcome to Python Programming\" " # \" is used to print double quotes or any Special characters in the string.
print(Escaped_String1)
print(Escaped_String2)
print(Escaped_String3)

# Find the example of Using Special Characters in pythonm Without Escaping. We can use special characters in python without escaping by using 
# single quotes for the string if we want to use double quotes in the string and double quotes for the string if we want to use single quotes in the string. 
# Find Example Below
Special_Character_String1 = ' Hello Mr. Rahul Vajpayee, "Welcome to Python Programming" ' # We can use double quotes in the string by using single quotes for the string.
Special_Character_String2 = " It's a nice day to learn Python Programming " # We can use single quotes in the string by using double quotes for the string.
print(Special_Character_String1)
print(Special_Character_String2)
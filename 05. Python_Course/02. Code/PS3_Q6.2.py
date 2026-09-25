# Take a user input string and check if it is a palindrome (same forwards and backwards).
print("welcome to the String Palindrome Check Program.".title())
_string = input("Please Enter your string. : ".title())
_revstring = _string[::-1]
if _string == _revstring:
    print("You have entered a Palindrome String.".title())
else:
    print("Your String is not palindrom string.".title())
end = input("Thanks for using the Program".title())
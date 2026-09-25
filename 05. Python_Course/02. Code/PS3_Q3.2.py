# Check if the string "123abc" is alphanumeric.
# Solution ==>

print("Welcome to Check the String Type Program.")
s1 = input("Please Enter your String to check its Type. :")

if s1.isalpha()==True:
    print("your string is albhabetic in nature")
elif s1.isnumeric()==True:
    print("your string is numeric in nature")
elif s1.isalnum()==True:
    print("your string is albhanumeric in nature")
end = input("Hit Enter to Exit The Program.")

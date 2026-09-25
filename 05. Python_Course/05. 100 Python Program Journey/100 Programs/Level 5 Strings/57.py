# 57. Remove spaces from string
# Solution ==>

def greet():
    print("Welcome to Remove spaces from string Program.!!")

def remove_spaces(_string):
    i = 0
    new_String = ""
    while i <= (len(_string)-1):
        if _string[i] != " ":
            i +=1
        else:
            new_String = _string.replace(" ", "")
            return new_String           
    return "No Space Found." 


greet()
_string = input("Please Enter your String to Remove Spaces. : ")

print(remove_spaces(_string))

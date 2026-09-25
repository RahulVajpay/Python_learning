# 53. Convert uppercase to lowercase
# Solution ==>

def greet():
    print("Welcome to Uppercase to lowercase String Convert Program.!!")

def upper_to_lower(_string):
    revised_str = ""
    i = 0
    while i <= len(_string)-1:
        if _string[i] == _string[i].upper():
            revised_str = revised_str + _string[i].lower()
            i +=1
        else:
            revised_str = revised_str + _string[i]
            i+=1 
    return f'Your String "{_string}" is Converted to "{revised_str}"'

greet()
_string = input("HI Dear Please Enter your String. : ")

print(upper_to_lower(_string))

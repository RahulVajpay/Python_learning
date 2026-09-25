# 52. Convert lowercase to uppercase
# Solution ==>

def greet():
    print("Welcome to lowercase to Uppercase String Convert Program.!!")

def lower_to_upper(_string):
    revised_str = ""
    i = 0
    while i <= len(_string)-1:
        if _string[i] == _string[i].lower():
            revised_str = revised_str + _string[i].upper()
            i +=1
        else:
            revised_str = revised_str + _string[i]
            i+=1 
    return f'Your String "{_string}" is Converted to "{revised_str}"'

greet()
_string = input("HI Dear Please Enter your String. : ")

print(lower_to_upper(_string))

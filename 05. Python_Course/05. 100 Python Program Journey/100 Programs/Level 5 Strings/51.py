# 51. Count spaces
# Solution ==>

def greet():
    print("Welcome to Count spaces in a String Program.!!")

def count_spaces(_string):
    count = 0
    i = 0
    while i <= len(_string)-1:
        if _string[i].lower() in (' '):
             count +=1
             i +=1
        else:
            i+=1 
    return f'Total Number of spaces in Your String "{_string}" is {count}'

greet()
_string = input("HI Dear Please Enter your String. : ")

print(count_spaces(_string))
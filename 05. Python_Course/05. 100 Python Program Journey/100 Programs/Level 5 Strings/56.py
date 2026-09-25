# 56. Count occurrence of character
# Solution ==>

def greet():
    print("Welcome to Count occurrence of character in string Program.!!")

def count_occ_char(_string, char):
    i = 0
    count = 0
    while i <=(len(_string)-1):
        if _string[i].lower() == char.lower():
            count += 1
            i +=1
        else:
            i +=1
    return f'Total Number of "{char}" in your String "{_string}" is {count}.'

greet()
_string = input("Please Enter your String              : ")
_char   = input("Please Enter your Character to search : ")

print(count_occ_char(_string, _char))
            




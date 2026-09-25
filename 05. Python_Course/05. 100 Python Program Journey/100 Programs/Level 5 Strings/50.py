# 50. Count consonants
# Solution ==>

def greet():
    print("Welcome to Count consonants in a String Program.!!")

def count_consonants(_string):
    count = 0
    i = 0
    while i <= len(_string)-1:
        if _string[i].isalpha() and _string[i].lower() not in ("a", "e", "i", "o", "u"):
             count +=1
             i +=1
        else:
            i+=1 
    return f'Total Number of consonants in Your String "{_string}" is {count}'

greet()
_string = input("HI Dear Please Enter your String. : ")

print(count_consonants(_string))
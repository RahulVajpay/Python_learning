# 49. Count vowels
# Solution ==>

def greet():
    print("Welcome to Count Vowels in a String Program.!!")

def count_vowels(_string):
    count = 0
    i = 0
    while i <= len(_string)-1:
        if _string[i].lower() in ('a', 'e', 'i', 'o', 'u'):
             count +=1
             i +=1
        else:
            i+=1 
    return f'Total Number of Vowels in Your String "{_string}" is {count}'

greet()
_string = input("HI Dear Please Enter your String. : ")

print(count_vowels(_string))
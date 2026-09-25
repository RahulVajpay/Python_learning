# 47. Reverse string
# Solution ==>

def greet():
    print("Welcome to Reverse String Program.!!")

def reverse_string(_string):
    rev_str = ""
    i = 0
    while i <= len(_string)-1:
        rev_str = _string[i] + rev_str
        i +=1
    return rev_str

greet()
_string = input("HI Dear Please Enter your String. : ")

print(reverse_string(_string))
    
        



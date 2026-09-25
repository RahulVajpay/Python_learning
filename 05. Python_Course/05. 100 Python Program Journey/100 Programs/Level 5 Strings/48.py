# 48. Check palindrome string


def greet():
    print("Welcome to Palindrome string Check Program.!!")

def palindrome_string(_string):
    rev_str = ""
    i = 0
    while i <= len(_string)-1:
        rev_str = _string[i] + rev_str
        i +=1
    if _string.lower() == rev_str.lower():
            return f"You have Entered a Palindrom String."
    else:
         return f"You have Entered a Non Palindrom String."

greet()
_string = input("HI Dear Please Enter your String. : ")

print(palindrome_string(_string))
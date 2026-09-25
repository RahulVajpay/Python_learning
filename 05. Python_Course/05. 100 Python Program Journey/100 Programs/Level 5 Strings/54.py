# 54. Find substring
# Solution ==>

def greet():
    print("Welcome to Find substring in a  String Program.!!")

def find_substring(_string, _substring):
    conveted_string = _string.lower()
    converted_substring = _substring.lower()
    if conveted_string.find(converted_substring)>= 0:
        return f'Your substring "{_substring}" is found at the index of {conveted_string.find(converted_substring)} at your String "{_string}".'
    else:
        return f'Your substring "{_substring}" is not found in your String "{_string}".'

   

greet()
_string = input("HI Dear Please Enter your String. : ")
_substring = input("HI Dear Please Enter your SubString. : ")

print(find_substring(_string, _substring))



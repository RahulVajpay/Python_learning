# 55. Replace word in string
# Solution ==>

def greet():
    print("Welcome to Replace word in string Program.!!")

def replace_word(_string, fword, rword):
     conveted_string = _string.lower()
     converted_substring = fword.lower()
     if conveted_string.find(converted_substring)>= 0:
            print(f'"{fword}" Word found Successfully in your string "{_string}".')
            _UpdatedString = _string.replace(fword, rword, -1)
            return f'Your Updated Version of string "{_string}" is "{_UpdatedString}"'
     else:
         return f'Your Find Word "{fword}" is not found in your String "{_string}".'     


greet()
_string = input("HI Dear Please Enter your String.                   : ")
_fword =  input("HI Dear Please Enter your Word to be Replaced.      : ")
_rword =  input("HI Dear Please Enter your Word which to be Replaced : ")

print(replace_word(_string, _fword , _rword))

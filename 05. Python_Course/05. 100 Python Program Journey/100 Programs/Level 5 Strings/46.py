# 46. Count characters in string
# Solution ==>

def greet():
    print("Welcome to Count characters in string Program !!")

def count_characters(_string):
    count = 0
    for char in _string:
        count +=1
    return count

greet()
_string = input("HI Dear Please Enter your String. : ")

print(f"Total Number of characters is your Strings is {count_characters(_string)}")

    




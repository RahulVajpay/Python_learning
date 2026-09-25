# 60. Find duplicate characters
# Solution ==>

def greet():
    print("Welcome to Find duplicate character in string Program.!!")

def find_duplicate_characters(_string):
    i = 0
    All_list = []
    dup_list = []
    while i <= len(_string)-1:
        if _string[i] not in All_list:
            All_list.append(_string[i].lower())
            i +=1
        elif _string[i] not in dup_list:
            dup_list.append(_string[i].lower())
            i +=1
        else:
            i +=1    
    return dup_list  

greet()
_string = input("Please Enter your String to Find Dupicate Words. : ")

print(find_duplicate_characters(_string))          

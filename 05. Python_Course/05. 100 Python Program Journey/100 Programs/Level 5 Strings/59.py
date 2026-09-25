# 59. Check anagram
# Solution ==>

def greet():
    print("Welcome to Check Anagram Program.!!")

def check_anagram(word1, word2):
    word1_lsit = []
    word2_list = []
    for char in word1:
        word1_lsit.append(char.lower())
    for char in word2:
        word2_list.append(char.lower())
    if sorted(word1_lsit) == sorted(word2_list):
        return f'Your Words "{word1}" , "{word2}" are Anagram.'
    else:
        return f'Your Words "{word1}" , "{word2}" are not Anagram.'

greet()
word1 = input("Please Enter your First Word.  : ")
word2 = input("Please Enter your Second Word. : ")

print(check_anagram(word1, word2))
        
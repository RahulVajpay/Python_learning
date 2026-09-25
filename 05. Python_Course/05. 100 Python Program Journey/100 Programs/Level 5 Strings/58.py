# 58. Find longest word
# Solution ==>

def greet():
    print("Welcome to Find longest word in string Program.!!")

def longest_word(_string):
    wordlist = _string.split(" ")
    i = 0
    _maxlen = 0
    _maxword = ''
    while i <= len(wordlist) - 1:
        if len(wordlist[i]) > _maxlen:
            _maxlen = len(wordlist[i])
            _maxword = wordlist[i]
            i +=1
        else:
            i +=1    
    return f'The Longest Word in your String "{_string}" is "{_maxword}" which have "{_maxlen}" Characters.'

greet()
_string = input("Please Enter your String to Find the Longest Word.: ")

print(longest_word(_string))



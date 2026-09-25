print('Welcome to Multiple input in single line ceode Program Example.')
# Taking multiple input in single line
# input() function takes input as string, so we need to convert it into integer using map
# map() function takes two arguments, first is the function and second is the iterable
# Here we are using int() function to convert the input into integer and split() function to
# split the input into list of strings
a, b, c = input('Enter three numbers separated by space: ').split()
print((a), (b) , (c))
word = 'geeks, for, geeks, hello'

print(word.split(', ', 0)) 
print(word.split(', ', 4))  
print(word.split(', ', 1))
# Given text = "Python Programming" , do the following:
# Print the first 6 characters.
# Print the last 6 characters.
# Print every second character from the string
# Solution ==>

s1 = "Python Programming"
print(s1[0:6]) # Print the first 6 characters.
print(s1[len(s1)-6:len(s1)]) # Print the last 6 characters.
print(s1[1:len(s1):2]) #Print every second character from the string (This is Called Step Method Which Basically string[start:end:step] Works as (step-1) Word Jump)

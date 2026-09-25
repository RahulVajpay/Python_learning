# Using format() , create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.
# Solution ==>

s1 =  "My name is {} and I am {} years old."
name1 = input("please enter your name. : ".title())
age1  = input("please enter your age.  : ".title())

print(s1.format(name1,age1))

# Write a program that counts how many vowels are in a given string.
# Solution ==>
print("Welcome to the Program Which Counts Vowels in a String.".title())
_string = input("Please Enter your string. : ".title())
count = 0
for i in range(len(_string)):
    if _string[i] in ("a", "e", "i", "o", "u"):
        count+=1
print(f"Total Number of Vowel is {count}")

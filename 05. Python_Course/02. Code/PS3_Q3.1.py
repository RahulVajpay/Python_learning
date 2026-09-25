# Take the string " i love python programming " and:
# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears
# Solution ==>

s1 = " i love python programming "

print(s1.lstrip().rstrip())   # Remove extra spaces from both ends
print(s1.title())             # Convert it to title case

count = 0
for i in range(len(s1)):
    if s1[i] == "o":
        count +=1
print(f'Total number of "o" is {count}')
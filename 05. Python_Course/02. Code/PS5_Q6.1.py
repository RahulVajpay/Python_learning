# Write a program that takes a list of numbers and removes all duplicates using a set.
# Solution ==>


_list = [0,1,2,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
_set = set()                       # Method to Create empty Set.

for i in range(0, len(_list)):
    _set.add(_list[i])
print(_set)

# Convert back to List
# Method 1
clean_list = list(_set)
clean_list.sort()
print(f"This is from method 1 : {clean_list}")

# Method 2

clean_list = []
for i in _set:
    clean_list.append(i)

clean_list.sort()
print(f"This is from method 2 : {clean_list}")
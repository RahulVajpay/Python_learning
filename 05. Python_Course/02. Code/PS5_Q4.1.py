# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3 ?)
# Add 5 to the set, remove 2 , and check if 4 is in the set.
# Solution ==>

my_set = {1, 2, 3, 3, 4}
print(my_set)
print("duplicate 3 value removes from set because set don't allow duplicate item.")

# Add 5 to the set, remove 2 , and check if 4 is in the set.
my_set.add(5)
my_set.remove(2)

check_set = {4}

if my_set.intersection(check_set) == check_set:
    print(f"4 is present in the my_Set = {my_set}")
else:
    print(f"4 is not present in my_set = {my_set}")
    
    


# Start with numbers = [5, 2, 9, 1, 7] and do the following:
# Sort the list in ascending order.
# Append the number 10 to the list.
# Remove the number 2 from the list.
#Solution ==>

numbers = [5, 2, 9, 1, 7]

print(f"This is Your Original List.             : {numbers}")

# Sort the list in ascending order.This method will change the Orginal List.
numbers.sort()                    
print(f"This is Your ascending order Sort List  : {numbers}")

# Sort the list in Descending order.This method will change the Orginal List.
numbers.sort(reverse=True)                    
print(f"This is Your Descending order Sort List : {numbers}")

# Append the number 10 to the list.
numbers.append(10)
print(numbers)

# Remove the number 2 from the list.
numbers.remove(2)   # remove method used to remove a particular item from list. Pop is used to Remove the Element at a Particular Index.
print(numbers)


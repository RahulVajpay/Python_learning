# Create a list fruits = ["apple", "banana", "cherry"] .
# Print the first fruit.
# Replace "banana" with "orange" .
# Print the length of the list.
# Solution ==>

fruit = ["apple", "banana", "cherry"]

# Print the first fruit.
print(fruit[0])

# Replace "banana" with "orange" .
fruit[fruit.index("banana")] = "orange"
print(fruit)

# Print the length of the list.
print(len(fruit))
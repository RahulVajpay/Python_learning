# Create a tuple coordinates = (10, 20) and print both elements.
# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
# Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple.
# Solution==>

coordinates = (10, 20)
original_coordinates = coordinates
print(f"ID of tuple name 'coordinates': {id(coordinates)}")
print(f"ID of  tuple name 'original_coordinates': {id(original_coordinates)}")


# print both elements
print(f"{coordinates[0]}, {coordinates[1]}")

# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
print("coordinates[0] = 50 'tuple' object does not support item assignment")

list_cordinates = []

# Convert the tuple to a list
for i in range(0 , len(coordinates)):
    list_cordinates.append(coordinates[i])

list_cordinates.insert(0 , 50)   # Add Element 50 to List.
print(list_cordinates, type(list_cordinates))

# convert list back to a tuple. But this is not the original tuple, it is a new tuple with the same values as the list.
coordinates = tuple(list_cordinates)
print(coordinates, type(coordinates))
print(f"ID of new tuple coordinates: {id(coordinates)}")
print(f"As ID OF original tuple 'coordinates' and new tuple 'coordinates' are different, it means that a new tuple is created and original tuple is not changed.")
print("original_coordinates is not changed", original_coordinates)
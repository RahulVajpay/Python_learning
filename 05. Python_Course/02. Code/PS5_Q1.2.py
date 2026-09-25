# Create a list of numbers from 1 to 10 .
# Print the first three numbers using slicing.
# Print the last three numbers using slicing.

num_list = []

#  1   2  3  4  5  6  7  8  9  10
#  0   1  2  3  4  5  6  7  8   9   # Positive Index
# -10 -9 -8 -7 -6 -5 -4 -3 -2  -1   # Negative Index

# Create a list of numbers from 1 to 10 .
for x in range (1, 11):
    num_list.append(x)

# Print the first three numbers using slicing.
print(num_list[:3])     # PosItivse slicing USed for First Three Which Print index 0 to index 2

# Print the last three numbers using slicing.
print(num_list[-3:])  # negative slicing USed for last Three Which Print index -3 to index -1

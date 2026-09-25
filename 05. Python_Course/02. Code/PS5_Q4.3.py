# Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}
#Find their:
# Union
# Intersection
# Difference ( a - b )
# Solution ==>

a = {1, 2, 3}
b = {3, 4, 5}

#Union
Union = a.union(b)
print(f"Union of {a} and {b} is {Union}")

#Intersection
Intersection = a.intersection(b)
print(f"Intersection of {a} and {b} is {Intersection}")

# Difference ( a - b )
Difference = a.difference(b)
print(f"Difference of {a} and {b} is {Difference}")

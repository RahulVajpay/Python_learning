# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
# Solution
numbers = [1, 2, 3, 4, 5]
square =  list(map( lambda x : x * x , numbers[:2]))
print(square)

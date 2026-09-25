import functools as FT
l = []

for i in range(1, 10):
    l.append(i**2)



X = FT.reduce(lambda x, y: x + y, l)
print(X)
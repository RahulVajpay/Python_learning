# Write a program that merges two dictionaries into one.
# Solution ==>

dict1 = {"Rahul" : "7982362429" , "Rohit" : "9205954936" , "Papa" : "9873282433"}
dict2 = {"Sanjana" : "9792831483" , "Priya" : "9569665827" , "Garima" : "7355638500" , "Mummy" : "9310109285"}

# Adding Dictionary 2 in Dictionary 1
for item, value in dict2.items():
    dict1[item] = value

# Printing all Elements of Dictionary 1
for item , value in dict1.items():
    print(f"{item}\t:{value}")
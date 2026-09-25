# Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them

contact_dict = {"Rahul" : "7982362429" , "Rohit" : "9205954936" , "Papa" : "9873282433"}

# keys() to get all names
print(contact_dict.keys())

# values() to get all numbers
print(contact_dict.values())

# items() to loop over key-value pairs and print them

for key , value in contact_dict.items():
    print(key , value)

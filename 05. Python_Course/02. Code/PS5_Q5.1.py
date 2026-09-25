# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
# Print the value of "name" .
# Change "grade" to "A+" .
# Add a new key "city" with value "Delhi" .
# Solution ==>

student = {"name": "John", "age": 20, "grade": "A"}
ori_student = student
# Print the value of "name" .
print(student['name'])

# Change "grade" to "A+" .
student['grade'] = "A+"
print(student)

# Add a new key "city" with value "Delhi" .
student['city'] = "Delhi"
print(ori_student)
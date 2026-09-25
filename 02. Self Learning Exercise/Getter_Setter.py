class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property  # This decorator allows us to access the method as an attribute without parentheses
    def First_Name(self):
        l = self.name.split(" ")
        return l[0]
    
    @First_Name.setter # This decorator allows us to set the value of the property using assignment
    def First_Name(self, First_NewName):
        l = self.name.split(" ")
        NewName = f"{First_NewName} {l[1]}"
        self.name = NewName

emp1 = Employee("John Doe", 50000)
print(emp1.First_Name)  # Output: John
emp1.First_Name = "Jane" # This will call the setter method to update the name
print(emp1.name)  # Output: Jane Doe

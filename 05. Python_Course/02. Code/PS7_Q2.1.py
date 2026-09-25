# Create a class Employee with a private attribute _salary .
# Use @property to define a getter for salary .
# Use @salary.setter to prevent setting negative values (print a warning instead).
# Create an object and test by setting positive and negative salaries.
# Solution ==>

class Employee:

    def __init__(self, name, age, salary):
        self.Name = name
        self.Age = age
        self.Salary = salary

    @property
    def Getsalary(self):
       return self.Salary
    
    @Getsalary.setter
    def Setsalary(self, NewSalary):
        if NewSalary <=0:
            print("Invalid Salary Enter.")
        else:
           self.Salary = NewSalary


    def __str__ (self):
        return (f"The Name of Employee is {self.Name}, He is {self.Age} years Old and His Current CTC is {self.Salary}")   


e1 = Employee("Rahul", 30, 2500002)
print(e1.Getsalary)
e1.Setsalary = 350000000
print(str(e1))


        
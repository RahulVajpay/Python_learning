# Create a class Person with a constructor (__init__ ) that accept name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.
# Solution ==>

class Person:
    def __init__(self, name , age):
        self.Name = name
        self.Age  = age

    def getinfo (self):
        return f'Hi {self.Name} !! You are {self.Age} years old.'
    
P1 = Person('Rahul Vajpay' , 31)
print(P1.getinfo())
    
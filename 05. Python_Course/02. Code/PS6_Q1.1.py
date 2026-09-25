# Create a class Car with a method drive() that prints "Car is moving" Create an object of Car and call drive()
# Solution ==>

class Car: 
    def drive(self):        
        return "Car is moving"
    def parked(self):        
        return "Car is parked"

c1 = Car()
c2 = Car()
print(c1.drive())
print(c2.parked())
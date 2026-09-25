# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!" .
# Create an object of Dog and call sound().
# Solution ==> 

class Animal:
    def __init__(self , name):    # Are Constructors.
        self.Name = name

    def sound(self):              # Are Method/Function in Class
        print("Some sound")

class Dog(Animal):               # Dog Class Inherited from Parent Class Animal
    def sound(self ):            # Sound Method Overrides the Parent class  Sound method
        super().sound()          # Mehod to Call Parent Class Method to Child Class.
        print(f"{self.Name} is Barking !! ")
        
D1 = Dog('Bruno')
D1.sound()
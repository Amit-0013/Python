##Create a base class named `Animal` with attributes `name` and `species`.
#Create a derived class named `Dog` that inherits from `Animal` and adds an attribute `breed`. 
#Create an object of the `Dog` class and print its attributes.
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
##In the `Dog` class, override the `__str__` method to return a string representation of the object. 
#Create an object of the class and print it.

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed = breed
    def __str__(self):
        return f"Dog Name: {self.name} , Dog Breed: {self.breed}"
    ##In the `Dog` class, add a method named `bark` that prints a barking sound. Create an object of the class and call the method.
    def bark(self):
        print("Woof")
d1 = Dog("Tomy","NA","labra")
print(d1.name)
print(d1.species)
print(d1.breed)
print(d1)
d1.bark()

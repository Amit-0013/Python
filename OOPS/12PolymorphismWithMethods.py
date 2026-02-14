##Create a base class named `Shape` with a method `area`. 
#Create two derived classes `Circle` and `Square` that override the `area` method. 
#Create a list of `Shape` objects and call the `area` method on each object to demonstrate polymorphism.
import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius **2
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return 4 * self.length
shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area())
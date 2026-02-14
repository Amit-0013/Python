##Create an abstract base class named `Shape` with an abstract method `area`. 
#Create derived classes `Circle` and `Square` that implement the `area` method. 
#Create objects of the derived classes and call the `area` method.
from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area():
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
        return 4* self.length
c1 = Circle(5)
s1 = Square(5)
print(c1.area())
print(s1.area())

    

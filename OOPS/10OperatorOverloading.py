##Create a class named `Vector` with attributes `x` and `y`. Overload the `+` operator to add two `Vector` objects. 
#Create objects of the class and test the operator overloading.
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y = y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"{self.x} , {self.y}"
v1 = Vector(2,3)
v2 = Vector(3,5)
v3 = v1+v2
print(v3)
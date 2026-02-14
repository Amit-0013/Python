##Create a class named `A` with a method `show` that prints a message. 
#Create two derived classes `B` and `C` that inherit from `A` and override the `show` method. 
#Create a class `D` that inherits from both `B` and `C`. Create an object of the `D` class and call the `show` method. 
#Observe the method resolution order.

class A:
    def show(self):
        print("A's Show")
class B(A):
    def show(self):
        print("b's Show")
class C(A):
    def show(self):
        print("C's Show")
class D(B,C):
    pass

d = D()
d.show()


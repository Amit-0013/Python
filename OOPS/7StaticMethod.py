##Create a class named `MathOperations` with a static method to calculate the square root of a number. 
#Call the static method without creating an object.
import math
class MathOperation:
    @staticmethod
    def square_root(x):
        return math.sqrt(x)
print(MathOperation.square_root(25))
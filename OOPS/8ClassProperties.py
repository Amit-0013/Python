##Create a class named `Rectangle` with private attributes `length` and `width`. Use properties to get and set these attributes. 
#Create an object of the class and test the properties.
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def set_length(self,__length):
        self.__length = __length
        print(f"New length is: {self.__length}")

    def get_length(self):
        return self.__length
    
    def set_width(self,__width):
        self.__width = __width
        print(f"New Width is: {self.__width}")

    def get_width(self):
        return self.__width
    
r1 = Rectangle(25,30)
print(r1.get_length())
r1.set_length(40)
print(r1.get_width())
r1.set_width(20)


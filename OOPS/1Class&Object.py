##Create a class named `Car` with attributes `make`, `color`, and `year`. Create an object of the class and print its attributes.
##Add a method named `start_engine` to the `Car` class that prints a message when the engine starts. 
#Create an object of the class and call the method.
class car:
    def __init__(self,make,color,year):
        self.make = make
        self.color = color
        self.year = year
    def start_engine(self):
        print(f"The engine of the car {self.make} has started.")
swift = car("Swift","White",2022)
print(swift.make)
print(swift.color)
print(swift.year)
swift.start_engine()


    
    
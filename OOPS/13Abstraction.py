##Create an abstract base class named `Vehicle` with an abstract method `start_engine`. 
#Create derived classes `Car` and `Bike` that implement the `start_engine` method. 
#Create objects of the derived classes and call the `start_engine` method.

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine():
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car is starting.")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike is starting.")
c1 = Car()
c1.start_engine()
b1 = Bike()
b1.start_engine()
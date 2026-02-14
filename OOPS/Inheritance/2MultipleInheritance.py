##Create a base class named `Walker` with a method `walk` that prints a walking message. 
#Create another base class named `Runner` with a method `run` that prints a running message. 
#Create a derived class named `Athlete` that inherits from both `Walker` and `Runner`. 
#Create an object of the `Athlete` class and call both methods.

class Walker:
    def walk(self):
        print("I am walking.")
class Runner:
    def run(self):
        print("I am running.")
##In the `Athlete` class, override the `walk` method to print a different message. 
#Create an object of the class and call the `walk` method. 
#Use the `super()` function to call the `walk` method of the `Walker` class.

##In the `Athlete` class, add an attribute `training_hours` and a method `train` that prints the training hours. 
#Create an object of the class and call the method.
class Athlete(Walker,Runner):
    def walk(self):
        super().walk()
        print("Walking is just for warmup.")
    def __init__(self,training_hours):
        self.training_hours = training_hours
    def train(self):
        print(f"The duration of training is: {self.training_hours}")
a1 = Athlete(5)
a1.run()
a1.walk()
a1.train()
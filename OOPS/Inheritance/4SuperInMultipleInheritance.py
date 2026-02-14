#Create a class named `Person` with an attribute `name`. 
#Create a class named `Employee` with an attribute `employee_id`. 
#Create a derived class `Manager` that inherits from both `Person` and `Employee`. 
#Use the `super()` function to initialize the attributes. 
#Create an object of the `Manager` class and print its attributes.
class Person:
    def __init__(self,name):
        self.name = name
class Employee:
    def __init__(self,employee_id):
        self.employee_id = employee_id
class Manager(Person,Employee):
    def __init__(self,name,employee_id,age):
        super().__init__(name)
        Employee.__init__(self,employee_id)
        self.age = age
m1 = Manager("Amit",21,101)
print(m1.age)
print(m1.name)
print(m1.employee_id)

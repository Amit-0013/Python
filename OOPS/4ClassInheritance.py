##Create a base class named `Person` with attributes `name` and `age`. 
#Create a derived class named `Employee` that inherits from `Person` and adds an attribute `employee_id`. 
#Create an object of the derived class and print its attributes.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
##In the `Employee` class, override the `__str__` method to return a string representation of the object. 
#Create an object of the class and print it.
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
    def __str__(self):
        return f"Employee Name: {self.name} , Employee Age: {self.age} , Employee ID: {self.employee_id}"
        
e1 = Employee("Amit",21,101)
print(e1.name)
print(e1.age)
print(e1.employee_id)
print(e1)

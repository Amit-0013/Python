##Create a class named `Address` with attributes `street`, `city`, and `pin`. 
#Create a class named `Person` that has an `Address` object as an attribute. 
#Create an object of the `Person` class and print its address.
class Address:
    def __init__(self,street,city,pin):
        self.street = street
        self.city = city
        self.pin = pin
class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
add = Address("11A","BKSC",827013)
per = Person("Amit",21,add)
print(per.address.street,per.address.city,per.address.pin)

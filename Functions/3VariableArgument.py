##Define a function that takes a variable number of keyword arguments and returns a dictionary containing 
# only those key-value pairs where the value is an integer. Test the function with different inputs.

def Filter_dict(**kwargs):
    for key,value in kwargs.items():
        if  isinstance(value,int):
            print(f"{key}:{value}")
Filter_dict(a=1,b="Two",c=4.5)
Filter_dict(a=2,b="Two",c=4,d=99,e=101,f=9.9)
##Define a function that takes two arguments, a and b, where b is a dictionary with a default value of an empty dictionary. 
# The function should add a new key-value pair to the dictionary and return it.  Test the function with different inputs.

def add_to_dict(a,b = None):
    if b is None:
        b = {}
    b[a] = a**2
    return b

print(add_to_dict(2))
print(add_to_dict(3 ,{1:1}))
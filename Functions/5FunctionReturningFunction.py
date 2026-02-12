##Define a function that returns another function. The returned function should take an integer and return its square. 
# Test the returned function with different inputs.

def outer():
    def inner(n):
        return n**2
    return inner
square = outer()
print(square(2))

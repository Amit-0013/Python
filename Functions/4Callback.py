##Define a function that takes another function as a callback and a list of integers. 
# The function should apply the callback to each integer in the list and return a new list with the results. 
# Test with different callback functions.

def my_callback(callback,lst):
    return[callback(x) for x in lst]

print(my_callback(lambda x:x**2,[1,2,3,4] ))

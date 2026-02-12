##Create a dictionary with the first 5 positive integers as keys and their squares as values.
#  Convert the dictionary to a list of tuples and print it.
dict = {i:i**2 for i in range(1,6)}
tup = list(dict.items())
print(tup)
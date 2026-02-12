##Create a dictionary with the first 10 positive integers as keys and their squares as values.
# Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
dict = {i:i**2 for i in range(1,11)}
new_dict = {k:v for k,v in dict.items() if k%2==0}
print(new_dict)
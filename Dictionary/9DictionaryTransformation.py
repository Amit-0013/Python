##Create a dictionary with the first 5 positive integers as keys and their squares as values.
# Create a new dictionary with keys and values swapped. Print the new dictionary.
dict = {i:i**2 for i in range(1,6)}
swapped_dict = {v:k for k,v in dict.items()}
print(swapped_dict)
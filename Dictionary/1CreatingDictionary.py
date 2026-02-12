##Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.
my_dict = {i:i**2 for i in range(1,11)}
print(my_dict)

##Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
print("Value for key 5: ",my_dict.__getitem__(5))
print("All the keys: ",my_dict.keys())

##Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1.
#  Print the modified dictionary.
my_dict[11] = 121
del my_dict[1]
print("Modified List: ",my_dict)

##Iterate over the dictionary created in Assignment 1 and print each key-value pair.

print(my_dict.items())
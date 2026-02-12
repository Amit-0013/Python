##Create a dictionary where the keys are the first 5 positive integers and the values are lists 
# containing the first 5 multiples of the key. Print the dictionary.
dict = {i:[i*j for j in range(1,6)] for i in range(1,6)}
print(dict)
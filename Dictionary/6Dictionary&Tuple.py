##Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square.
#  Print the dictionary.
dict = {i:(i,i**2)for i in range(1,6)}
print(dict)
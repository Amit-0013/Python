##Create two dictionaries: one with keys as the first 5 positive integers and values as their squares,
# and another with keys as the next 5 positive integers and values as their squares. 
# Merge these dictionaries into a single dictionary and print it.
dict1 = {i:i**2 for i in range(1,6)}
dict2 = {i:i**2 for i in range(6,11)}
merged_dict = {**dict1 ,**dict2}
print("The merged dictionary is: ",merged_dict)
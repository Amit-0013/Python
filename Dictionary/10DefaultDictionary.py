##Create a default dictionary where each key has a default value of an empty list. 
# Add some elements to the lists and print the dictionary.
from collections import defaultdict

default_dict = defaultdict(list)
default_dict['a'].append(1)
default_dict['a'].append(2)
default_dict['b'].append(3)
print(default_dict)
##Write a function that takes a dictionary and a key as input and returns the value associated with the key. 
#Use try, except, and finally blocks to handle KeyError if the key is not found in the dictionary and print an appropriate message.

def value(dict,key):
    try:
        val = dict[key]

    except KeyError as e:
        print("Key not found: ",e)
        val = None
    finally:
        return val
print(value({'a': 1,'b': 2,'c': 3},'b'))

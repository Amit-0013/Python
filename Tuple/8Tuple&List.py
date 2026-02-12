##Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
tup = (1,2,3,4,5)
lst = list(tup)
lst.append(6)
new_tup = tuple(lst)
print(new_tup)
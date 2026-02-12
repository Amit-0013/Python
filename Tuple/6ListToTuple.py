##Convert a list of the first 5 positive integers to a tuple. Print the tuple.
lst = []
for i in range(1,6):
    lst.append(i)
tup = tuple(lst)
print(tup)
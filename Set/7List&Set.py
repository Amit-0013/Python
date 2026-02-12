##Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set.
#  Print the resulting set.
st = {1,2,3,4,5}
lst = list(st)
lst.append(6)
new_st = set(lst)
print("Resulting set: ",new_st)
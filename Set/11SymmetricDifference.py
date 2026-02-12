##Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set
st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8,9}
st2.symmetric_difference_update(st1)
print(st2)
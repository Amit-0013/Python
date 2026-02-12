##Create two sets: one with the first 5 positive integers and another with the first 5 even integers.
#  Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
st1 = {1,2,3,4,5}
st2 = {2,4,6,8,10}
union_set = st1.union(st2)
intersect_set = st1.intersection(st2)
difference_set = st1.difference(st2)
symmetric_set = st1.symmetric_difference(st2)
print("After union operation: ",union_set)
print("After intersection operation: ",intersect_set)
print("After difference operation: ",difference_set)
print("After symmetric difference operation: ",symmetric_set)

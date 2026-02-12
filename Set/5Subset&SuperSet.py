##Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. 
# Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.
set1 = {1,2,3,4,5}
set2 = {1,2,3}
print(set2.issubset(set1))
print(set2.issuperset(set1))
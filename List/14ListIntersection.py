##Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.
def intersect(lst1,lst2):
    return [x for x in lst1 if x in lst2]
lst1 = [1,2,3,4,5]
lst2= [4,5,6,7,8]
new_lst = intersect(lst1,lst2)
print(f"Common elements of both sets are: {new_lst}")

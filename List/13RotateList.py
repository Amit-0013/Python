##Write a function that rotates a list by n positions. Print the original and rotated lists.
def rotate(lst,n):
    return lst[n:]+lst[:n]
lst = [1,2,3,4,5]
rotate_list = rotate(lst,2)
print(f"Original List: {list}")
print(f"Rotated List: {rotate_list}")

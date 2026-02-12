##Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
def rev_list(lst):
    return lst[::-1]
lst = [1,2,3,4,5]
reversed = rev_list(lst)
print(f" Original List: {lst}")
print(f" Reversed List: {reversed}")
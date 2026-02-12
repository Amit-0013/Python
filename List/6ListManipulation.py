##Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
list =[]
for i in range(1,11):
    list.append(i)
print(list)
list.remove(2)
list.remove(4)
list.remove(6)
list.insert(5 ,99)
print(list)

##Create a tuple with the first 10 positive integers. Print the tuple.
nums = []
for i in range(1,11):
    nums.append(i)
tup = tuple(nums)
print(tup)

##Print the first, middle, and last elements of the tuple created in Assignment 1.
print("First: ",tup[0])
print("Last: ",tup[-1])
print("Middle: ",tup[4])

##Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.
print("First Three: ",tup[:4])
print("From index 2 to 5: ",tup[2:6])
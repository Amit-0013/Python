##Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
import random
n = int(input("Enter number of elements in list: "))

list = [random.randint(1,100) for i in range(n)]
unique_list = []
for num in list:
    if num not in unique_list:
        unique_list.append(num)
A_list = sorted(unique_list)
D_list = sorted(unique_list,reverse=True)
print("List with duplicates: ",list)
print("List without duplicates: ",unique_list)
print("Sorted in ascending order: ",A_list)
print("Sorted in descending order: ",D_list)
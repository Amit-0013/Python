##Write a Python program to sort a list of numbers in ascending order.
n = int(input("How many numbers in list: "))
numbers = []
for i in range(n):
    i = int(input("Enter the number: "))
    numbers.append(i)

print("Before Sorting: ",numbers)
numbers.sort()
print("After sorting: ",numbers)




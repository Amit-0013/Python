##Create a list of the first 20 positive integers. Print the list
n = int(input("How many numbers in the list: "))
nums = [int(input("Enter the number: "))for i in range(n)]
print(nums)
##Print the first, middle, and last elements of the list created in Assignment 1.
print("First: ",nums[0])
print("Last: ",nums[-1])
print("Middle: ",nums[n//2 - 1])
##Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
print("First Five: ",nums[0:5])
print("5 to 15: ",nums[5:16])


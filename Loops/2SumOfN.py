## Write a Python program to find the sum of the first n natural numbers.
n = int(input("Enter a number upto which sum is to be printed: "))
sum = 0
for i in range(n+1):
    sum += i
print("The sum of first N natural number is: ",sum)
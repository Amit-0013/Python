##Write a Python program to calculate the factorial of a number.
num = int(input("Enter a number: "))
result = 1
for i in range(1,num+1):
    result = result*i
print("The factorial of number is : ",result)
##Write a Python program to swap the values of two variables.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: ",num1 , num2)
temp = num1
num1 = num2
num2 = temp
print("After swapping: ",num1 , num2)

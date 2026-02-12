##Write a program that calculates the factorial of a number input by the user using a while loop.
num = int(input("Enter a number: "))
i = 1
result = 1
while i<=num:
    result = result * i
    i += 1
print("The factorial of the number is: ",result)
##Write a program that prints the first n Fibonacci numbers, where n is input by the user.
num = int(input("Enter a number: "))
a = 0
b = 1
for i in range(num):
    print(a , end=" ")
    temp = a
    a = b
    b = temp+b
    
    
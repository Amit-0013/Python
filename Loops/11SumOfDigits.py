##Write a program that calculates the sum of the digits of a number input by the user using a while loop.
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    ld = num%10
    sum+=ld
    num//=10
print("The sum of digits of the number is: ",sum)
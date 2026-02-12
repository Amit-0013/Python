##Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.
sum = 0
while True:
    num = int(input("Enter a number: "))
    sum = sum +num
    if num == 0:
        break
print("The of all entered number is: ",sum)
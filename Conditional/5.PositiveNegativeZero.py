##Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
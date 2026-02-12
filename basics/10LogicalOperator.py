##Write a Python program to demonstrate logical operators: and, or, not.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
##and
if num1 > num2 and num1%2==0:
    print("First number is greater and even.")
else:
    print("First number is either lesser or not even")
if num1 > num2 or num1%2==0:
    print("Either the first number is greater or even")
else:
    print("The first number is neither greater nor even.")
is_student = True
print(not is_student)
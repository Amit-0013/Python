##Write a program that checks if a number input by the user is a prime number using a for loop.
num = int(input("Enter a number: "))
count = 0
for i in range(2,num):
    if num%i==0:
        count =1
if num == 1:
   print("The number is neither prime nor composite.")
elif count == 0:
    print("The number is prime.")
else:
    print("The number is not prime.")
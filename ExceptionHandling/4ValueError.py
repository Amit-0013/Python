##Write a function that prompts the user to enter an integer. 
#Use try, except, and finally blocks to handle ValueError if the user enters a non-integer value and print an appropriate message.
def user_input():
    try:
        num = int(input("Enter a number od integer type: "))
        return num
    except ValueError as e:
        print("Please enter only integer type: ",e)
print(user_input())
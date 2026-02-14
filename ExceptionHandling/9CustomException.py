##Define a custom exception named `NegativeNumberError`. 
#Write a function that raises this exception if a negative number is encountered in a list.
#Use try, except, and finally blocks to handle the custom exception and print an appropriate message.

class NegativeNumberException(Exception):
    pass
def negative_num(lst):
    try:
        for num in lst:
            if num <0:
                raise NegativeNumberException("Negative Number found.",num)
    except NegativeNumberException as e:
        print("Negative number found: ",e)
print(negative_num([1,2,3,-1,-2]))
print(negative_num([1,2,3,4,5]))

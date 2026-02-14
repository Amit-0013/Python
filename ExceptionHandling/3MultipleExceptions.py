##Write a function that takes a list of integers and returns their sum. 
#Use try, except, and finally blocks to handle TypeError if a non-integer value is encountered and print an appropriate message.
def sum(lst):
    s = 0
    try:
        for i in lst:
            s +=i
    except TypeError as e:
        print("Please enter integer type only: ",e)
        s = None
    finally:
        return s
print(sum([1,2,3,4,5]))
print(sum([1,2,3,'a']))


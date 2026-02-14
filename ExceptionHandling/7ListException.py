##Write a function that takes a list and an index as input and returns the element at the given index. 
#Use try, except, and finally blocks to handle IndexError if the index is out of range and print an appropriate message.
def element(lst,index):
    try:
        return lst[index]
    except IndexError as e:
        print("Please enter the index within range: ",e)
        return None
    finally:
        print("Execution complete")

lst = [1,2,3,4,5,6,7,8,9,0]
print(element(lst,11))

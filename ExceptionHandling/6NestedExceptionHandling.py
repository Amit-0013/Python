##Write a function that performs nested exception handling. 
#It should first attempt to convert a string to an integer, and then attempt to divide by that integer. 
#Use nested try, except, and finally blocks to handle ValueError and ZeroDivisionError and print appropriate messages.
def multi(str):
    try:
        try: 
            n = int(str)
        except ValueError as e:
            print("Value error: ",e)
            n = None
        finally:
            print("Conversion attempt complete.")
        if n is not None:

            try:
                result = 10/n
            except ZeroDivisionError as e1:
                print("Cannot divide by zero: ",e1)
            finally:
                return result
    finally:
        print("Execution Complete")

print(multi('s'))
print('0')
print('12')
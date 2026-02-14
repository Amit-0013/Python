##Write a function that takes two integers as input and returns their division. 
#Use try, except, and finally blocks to handle division by zero and print an appropriate message.

def div(num1 , num2):
    try:
        result = num1/num2
    except ZeroDivisionError as e:
        print("Denominator cannot be 0.",e)
        result = None
    finally:
        print(result)
div(3,7)
div(10,0)
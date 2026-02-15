##Write a decorator named `time_it` that measures the execution time of a function. 
#Apply this decorator to a function that calculates the factorial of a number.
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"Execution time is : {start_time - end_time}")
        return result
    return wrapper
@time_it
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))


    
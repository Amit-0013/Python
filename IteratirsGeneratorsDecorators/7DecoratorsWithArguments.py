##Write a decorator named `repeat` that takes an argument `n` and repeats the execution of the decorated function `n` times. 
#Apply this decorator to a function that prints a message.
def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator
@repeat(5)
def say_hello(msg):
    print(msg)
say_hello("Hello")
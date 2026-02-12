##Define a recursive function to calculate the nth Fibonacci number using memoization. Test the function with different inputs.
def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))
print(fib(6))
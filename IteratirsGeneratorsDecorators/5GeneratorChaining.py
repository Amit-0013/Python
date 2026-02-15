##Write two generator functions: `even_numbers` that yields even numbers up to a limit, 
#and `squares` that yields the square of each number from another generator. 
#Chain these generators to produce the squares of even numbers up to 20.
def even_num(n):
    for i in range(n+1):
        if i % 2 ==0:
            yield i
def squares(numbers):
    for num in numbers:
        yield num**2
even_gen = even_num(20)
sq = squares(even_gen)
for s in sq:
    print(s)

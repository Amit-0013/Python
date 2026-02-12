##Import the `randint` function from the `random` module and use it to generate a random integer between 1 and 100.

from random import randint,shuffle
x= randint(1,100)
print(x)

##Use the `random` module to generate a list of 5 random numbers between 1 and 50 and shuffle the elements of a list.
random_numbers = [randint(1,50) for i in range(5)]
print(random_numbers)
lst = [1,2,3,4,5]
shuffle(lst)
print("Shuffled list: ",lst)
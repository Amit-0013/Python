##Create a class named `MyRange` that mimics the behavior of the built-in `range` function. 
#Implement the `__iter__` and `__next__` methods. 
#Test the class by using it in a for loop.
class MyRange:
    def __init__(self,start,end):
        self.start = start
        self.end  = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >self.end:
            raise StopIteration
        else:
            self.start +=1
            return self.start - 1
for i in MyRange(1,5):
    print(i)
        
##Write a function that reads the contents of a file named `data.txt` and prints each line in reverse order.

def rev(filename):
    with open(filename,'r') as file:
        text = file.readlines()
    for line in reversed(text):
        print(line.strip())
rev('data.txt')
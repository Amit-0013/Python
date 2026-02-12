##Write a function that reads the contents of a file named `sample.txt` and prints each line.
with open('sample.txt','r') as file:
    for line in file:
        print(line.strip())
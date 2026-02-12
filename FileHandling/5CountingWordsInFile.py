##Write a function that reads the contents of a file named `document.txt` and returns the number of words in the file.

def count(filename):
    with open('log.txt','r') as file:
        text = file.read()
        words = text.split()
        return len(words)
print(count('log.txt'))
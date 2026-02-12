##Write a function that reads the contents of a file named `stats.txt` and returns the number of lines, words, and 
# characters in the file.

def count(filename):
    with open(filename) as file:
        lines = file.readlines()
        words = sum(len(line.split())for line in lines)
        char = sum(len(line) for line in lines)
        
       
    return len(lines),words,char
line , word , char= count('data.txt')
print("Number of lines in the file is: ",line)
print("Number of words in the file is: ",word)
print("Number of characters in the file is: ",char)

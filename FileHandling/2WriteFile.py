##Write a function that writes a list of strings to a file named `output.txt`, with each string on a new line.

def write(lines,file):
    with open('output.txt','w') as file:
        for line in lines:
            file.write(line +"\n")
write(["hello" ,"Python"],'output.txt')
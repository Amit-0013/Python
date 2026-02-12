##Write a function that appends a given string to the end of a file named `log.txt`.

def append(str , file):
    with open(file,'a') as file:
        file.write("\n"+str)
append("By Amit Ojha",'log.txt')
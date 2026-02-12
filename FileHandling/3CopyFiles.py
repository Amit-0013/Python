##Write a function that copies the contents of a file named `source.txt` to a new file named `destination.txt`.

def copy(source , destination):
    with open(source,'r') as source_file:
        content = source_file.read()
    with open(destination,'a') as destination_file:
        destination_file.write(content)
copy('sample.txt','destination.txt')
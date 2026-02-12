##Write a function that copies the contents of a file named `source.txt` to a new file named `destination.txt`.

def copy(soucre , destination):
    with open('sample.txt','r') as source_file:
        content = source_file.read()
    with open('destination.txt','a') as destination_file:
        destination_file.write(content)
copy('sample.txt','destination.txt')
##Write a function that merges the contents of multiple files into a single file named `merged.txt`.

def merge(file1 , file2 , merged_file):
    with open(file1,'r') as file:
        text = file.read()
    with open(file2,'r') as new_file:
        content = new_file.read()
    with open(merged_file,'w') as merged:
        merged.write(text +" "+content)
merge('data.txt','log.txt','merged.txt')
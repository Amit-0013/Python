##Write a function that reads a binary file named `image.bin` and writes its contents to another binary file named `copy_image.bin`.

def bin_file(filename , copy_file):
    data = b'\x001\x002\x004'
    with open(filename,'wb') as file:
        file.write(data)
    with open(filename,'rb') as file:
        content = file.read()
    with open(copy_file,'wb') as file:
        file.write(content)
bin_file('image.bin','copy.bin')

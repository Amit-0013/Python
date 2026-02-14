##Write a function that reads the contents of a file named `data.txt`. 
#Use try, except, and finally blocks to handle file not found errors and ensure the file is properly closed.
def read_file(filename):
    try:
        with open(filename ,'r') as file:
            content = file.read()
        print(content)
    except FileNotFoundError as e:
        print("Unable to find the file: ",e)
    except Exception as e1:
        print("Some error occurred: ",e1)
    finally:
        try:
            file.close()
        except NameError as e2:
            pass
read_file('data.txt')
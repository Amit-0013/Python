import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")
def print_letter():
    for letter in "abcde":
        time.sleep(1)
        print(f"Letters: {letter}")
## Creating two thread
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)
t = time.time()
## Starting the thread
t1.start()
t2.start()
##waiting for the threads to complete
t1.join()
t2.join()
Tn = time.time()
print(f"Time taken is: {Tn-t}")


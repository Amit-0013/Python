import multiprocessing
import time
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i} is: {i**2}")
def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"The cube of the {i} is: {i**3}")
if (__name__ == "__main__"):
    ##Creating two process
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    ##Starting two threads
    t1 = time.time()
    p1.start()
    p2.start()

    ##Waiting for threads to complete
    p1.join()
    p2.join()
    t2 = time.time()
    print(f"Time taken {t2-t1}")


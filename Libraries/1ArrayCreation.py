### Assignment 1: Array Creation and Manipulation

# 1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. 
#Replace all the elements in the third column with 1.
# 2.Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.



import numpy as np
arr = np.random.randint(1,21, size=(5,5))
print("Original Array:\n ",arr)
arr[:,2] = 1
print("Modifies Array:\n ",arr)

arr2 = np.random.randint(1,17, size = (4,4))
print("original array 2:\n ",arr2)
np.fill_diagonal(arr2,0)
print("Modifies Array2: \n",arr2)

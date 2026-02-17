### Assignment 8: Fancy Indexing and Boolean Indexing

# 1. Create a NumPy array of shape (5, 5) filled with random integers. 
# Use fancy indexing to extract the elements at the corners of the array.

import numpy as np
array = np.random.randint(1,21,size = (5,5))
print("Original array: ",array)
corners = array[[0,0,-1,-1],[0,-1,0,-1]]
print("Corners element: ",corners)

# 2. Create a NumPy array of shape (4, 4) filled with random integers. 
# Use boolean indexing to set all elements greater than 10 to 10.

array2 = np.random.randint(1,21, size=(4,4))
print("Original array: \n",array2)
array2[array2>10] = 10
print("modified array: \n",array2)
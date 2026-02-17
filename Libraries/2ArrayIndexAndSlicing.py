### Assignment 2: Array Indexing and Slicing
# 1. Create a NumPy array of shape (6, 6) with values from 1 to 36. 
# Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.

import numpy as np
arr  = np.random.randint(1,37, size = (6,6))
sub_array = arr[2:4 , 1:3]
print("Original Array1: \n",arr)
print("Sub array: \n",sub_array)
# 2. Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
arr2 = np.random.randint(1,100, size=(5,5))
print(arr2[0,0])
print(arr2[0,4])
print(arr2[4,0])
print(arr2[4,4])

### Assignment 7: Advanced Array Manipulation

# 1. Create a NumPy array of shape (3, 3) with values from 1 to 9. Reshape the array to shape (1, 9) and then to shape (9, 1).

import numpy as np
arr1 = np.arange(1,10).reshape(3,3)
print("Original Array: \n",arr1)
reshape_array = arr1.reshape(1,9)
print("Reshaped array: \n",reshape_array)
reshape_array = arr1.reshape(9,1)
print("Reshaped array: \n",reshape_array)

# 2. Create a NumPy array of shape (5, 5) filled with random integers. Flatten the array and then reshape it back to (5, 5).
print("Part two of the question.")
arr2 = np.random.randint(1,21, size=(5,5))
flatten_array = arr2.flatten()
print("Flatten array : \n",flatten_array)
reshape_array = flatten_array.reshape(5,5)
print("Reshaped array is: \n",reshape_array)
##### Assignment 5: Broadcasting

# 1. Create a NumPy array of shape (3, 3) filled with random integers.
#  Add a 1D array of shape (3,) to each row of the 2D array using broadcasting.

import numpy as np
array = np.random.randint(1,51, size = (3,3))
row_array = np.random.randint(1,11, size=(3,))
result = array + row_array
print(result)

# 2. Create a NumPy array of shape (4, 4) filled with random integers. 
# Subtract a 1D array of shape (4,) from each column of the 2D array using broadcasting.
print("Part two of the program.")
arr = np.random.randint(1,51, size=(4,4))
col_array = np.random.randint(1,11, size=(4,))
result = arr - col_array
print(result)
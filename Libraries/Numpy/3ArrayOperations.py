### Assignment 3: Array Operations
# 1. Create two NumPy arrays of shape (3, 4) filled with random integers. 
# Perform element-wise addition, subtraction, multiplication, and division.

import numpy as np
arr1 = np.random.randint(1,11, size=(3,4))
print("Original Array1: \n",arr1)
arr2 = np.random.randint(1,11, size=(3,4))
print("Original array2: \n",arr2)
print("Element wise Addition: \n",(arr1+arr2))
print("Element wise Subtraction: \n",(arr1-arr2))
print("Element wise Multiplication: \n",(arr1*arr2))
print("Element wise Division: \n",(arr1/arr2))
# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.

arr3 = np.random.randint(1,17, size=(4,4))
print("Original array: \n",arr3)
row_sum = np.sum(arr3 , axis=1)
print("Row wise sum of first row: \n",row_sum)
col_sum = np.sum(arr3 , axis=0)
print("Sum of first column : \n",col_sum)

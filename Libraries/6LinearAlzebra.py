### Assignment 6: Linear Algebra

# 1. Create a NumPy array of shape (3, 3) representing a matrix. Compute its determinant, inverse, and eigenvalues.

import numpy as np
matrix = np.random.randint(1,51, size=(3,3))
determinant = np.linalg.det(matrix)
inverse = np.linalg.inv(matrix)
eigen_values = np.linalg.eigvals(matrix)
print("Determinant = ",determinant)
print("Inverse of the matrix is: \n",inverse)
print("Eigen Values of the matrix is: \n",eigen_values)

# 2. Create two NumPy arrays of shape (2, 3) and (3, 2). Perform matrix multiplication on these arrays.
print("Part two of the question.")

arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(1,7).reshape(3,2)
multi = np.dot(arr1,arr2)
print("Matrix multiplication: \n",multi)
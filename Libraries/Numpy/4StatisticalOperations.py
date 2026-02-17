### Assignment 4: Statistical Operations

# 1. Create a NumPy array of shape (5, 5) filled with random integers. 
#Compute the mean, median, standard deviation, and variance of the array.

import numpy as np
arr = np.arange(0,25).reshape(5,5)
print("The mean of the data is: ",np.mean(arr))
print("The median of the data is: ",np.median(arr))
print("The standard deviation of the data is: ",np.std(arr))
print("The variance of the data is: ",np.var(arr))

# 2. Create a NumPy array of shape (3, 3) with values from 1 to 9. 
# Normalize the array (i.e., scale the values to have a mean of 0 and a standard deviation of 1).
## Normalization = (array-mean)/ standard deviation
arr2 = np.arange(1,10).reshape(3,3)
m = np.mean(arr2)
std_dev = np.std(arr2)
normalized_array = (arr2 - m)/std_dev
print(normalized_array)
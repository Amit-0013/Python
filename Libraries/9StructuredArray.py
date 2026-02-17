### Assignment 9: Structured Arrays
# 1. Create a structured array with fields 'name' (string), 'age' (integer), and 'weight' (float). 
# Add some data and sort the array by age.

import numpy as np
data_type = [('name','U10'), ('age','i4'),('weight', 'f4')]
data = np.array([('Amit',24,80),('Rishi',22,70),('Harsh',23,70)],dtype=data_type)
print("Original data: \n",data)
sorted_data = np.sort(data,order= 'age')
print("Sorted data: \n",sorted_data)



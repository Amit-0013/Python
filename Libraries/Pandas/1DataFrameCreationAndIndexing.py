### Assignment 1: DataFrame Creation and Indexing

# 1. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. Set the index to be the first column.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,21, size=(6,4)),columns = ['a','b','c','d'])
print("Original DataFrame: \n")
print(df)
df.set_index('a')
print("DataFrame with new index \n")
print(df)

# 2. Create a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'. 
# Fill the DataFrame with random integers and access the element at row 'Y' and column 'B'.

df1 = pd.DataFrame(np.random.randint(1,21, size= (3,3)),columns =['A','B','C'],index =['X','Y','Z'])
element = df1.at['Y','B']
print("Element at row 'Y' and column 'B': ",element)
### Assignment 2: DataFrame Operations

# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. 
#Add a new column that is the product of the first two columns.


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1,21, size=(3,5)),columns=['V','W','X','Y','Z'],index=['A','B','C'])
print("Original DataFrame: \n",df)
df['D'] = df['V'] *df['W']
print("Modified Dataframe: \n",df)

# 2. Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers. Compute the row-wise and column-wise sum.

df1 = pd.DataFrame(np.random.randint(1,100, size = (4,3)))
print("Original DataFrame: \n",df1)
row_sum = df1.sum(axis=1)
col_sum = df1.sum(axis=0)
print("Row sum: \n",row_sum)
print("Column sum: \n",col_sum)

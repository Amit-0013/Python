### Assignment 3: Data Cleaning

# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. 
# Introduce some NaN values. Fill the NaN values with the mean of the respective columns.

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1,100,size=(5,3)),columns=['A','B','C'])
print("Original data frame: \n",df)
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
df.iloc[0,2] = np.nan
print("DataFrame with null values: \n",df)
df.fillna(df.mean(), inplace = True)
print("Filled Data frame: \n",df)

# 2. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. 
# Introduce some NaN values. Drop the rows with any NaN values.
df1 = pd.DataFrame(np.random.randint(1,100,size = (6,4)),columns=['A','B','C','D'])
print("Original Data Frame: \n",df1)
df1.iloc[0,1] = np.nan
df1.iloc[1,2] = np.nan
df1.iloc[0,2] = np.nan
print("DataFrame with null values: \n",df1)
df1.dropna(inplace=True)
print("Missing rows dropped: \n",df1)
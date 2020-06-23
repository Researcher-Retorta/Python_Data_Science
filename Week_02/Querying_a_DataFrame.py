# %% 
import pandas as pd
import numpy as np

# Importing csv file (no numbers regarding the rows and columns label)
df2 = pd.read_csv(r'C:\Users\fabio.retorta\Desktop\Python_Codes\Week_02\olympics.csv', index_col = 0, skiprows=1)

df2.head()

# printing the columns
df2.columns

# %%
# Changing the label names
for col in df2.columns:
    if col[:2]=='01':
        df2.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df2.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df2.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df2.rename(columns={col:'#' + col[1:]}, inplace=True) 

# In order to view the new header
df2.head()

# Analyzing the data through dataframe label and math operation
df2['Gold'] > 0


only_gold = df2.where(df2['Gold'] > 0)
only_gold.head()

only_gold['Gold'].count()

df2['Gold'].count()

only_gold = only_gold.dropna()
only_gold.head()

only_gold = df2[df2['Gold'] > 0]
only_gold.head()

len(df2[(df2['Gold'] > 0) | (df2['Gold.1'] > 0)])

df2[(df2['Gold.1'] > 0) & (df2['Gold'] == 0)]

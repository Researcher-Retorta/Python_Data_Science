# %%
import pandas as pd
import numpy as np

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

df['Location'] = None

costs = df['Cost']
costs

costs+=2 # using broadcasting
costs

# Printing all the dataframe
# print(df)
df

# %%
# Importing csv file
df1 = pd.read_csv(r'C:\Users\fabio.retorta\Desktop\Python_Codes\Week_02\olympics.csv')
df1.head()

print("\n") # blank line

# %%
# Importing csv file (no numbers regarding the rows and columns label)
df2 = pd.read_csv(r'C:\Users\fabio.retorta\Desktop\Python_Codes\Week_02\olympics.csv', index_col = 0, skiprows=1)
df2.head() 
print("\n") # blank line

# printing the columns
df2.columns

for col in df2.columns:
    if col[:2]=='01':
        df2.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df2.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df2.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df2.rename(columns={col:'#' + col[1:]}, inplace=True) 

df2.head()

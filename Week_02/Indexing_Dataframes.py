# %% 
import pandas as pd
import numpy as np

# Importing csv file (no numbers regarding the rows and columns label)
df2 = pd.read_csv(r'C:\Users\fabio.retorta\Desktop\Python_Codes\Week_02\olympics.csv', index_col = 0, skiprows=1)
df2.head()

# %%
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

# %%
df2['country'] = df2.index
df2 = df2.set_index('Gold')
df2.head()

# %%
df2 = df2.reset_index()
df2.head()

# %%
# Opening other database
df = pd.read_csv('census.csv')
df.head()

# %%
df['SUMLEV'].unique()

# %%
df=df[df['SUMLEV'] == 50]
df.head()

# %%
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()

# %%
df = df.set_index(['STNAME', 'CTYNAME'])
df.head()

# %%
df.loc['Michigan', 'Washtenaw County']

# %%
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]

# %%

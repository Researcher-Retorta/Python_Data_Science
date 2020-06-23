# %%
import pandas as pd
df = pd.read_csv('census.csv')
df

# %%
# First example - code pandorable
(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

# %%
# Second example - Tadrition way to code (isn't pandorable)
df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})

# %%
# Importing numpy library
# Calculate max & min ans gives the results through a series

import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

# %%
# Returns through a pandas series the min & max of the specfied rows, however it doesn't show all the columns of dataframe "df"
df.apply(min_max, axis=1)

# %%
# Adds max & min columns at the end of the dataframe
import numpy as np
def min_max2(row):
        data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
        row['max'] = np.max(data)
        row['min'] = np.min(data)
        return row
# The result is all the columns of dataframe "df" plus "max" & "min" columns
df.apply(min_max2, axis=1)

# %%
# using lambda
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
# It doesn't use the min_max function
df.apply(lambda x: np.max(x[rows]), axis=1)
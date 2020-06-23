# %%
import pandas as pd
import numpy as np
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df

# %%
# works but it isn't the better way
for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + ' have an average population of ' + str(avg))

# %%
# Faster way (better computational effort)
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))

# %%
#
df = df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

# %%
#
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

# Aggregate using callable, string, dict, or list of string/callables
df.groupby('STNAME').agg({'CENSUS2010POP': np.average})

# %%
# Dataframe groupby and Series groupby 
# (These objects behave different for agg.)
print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))

# %%
# Example with a Series
(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP']
    .agg({'avg': np.average, 'sum': np.sum}))

# %%
# Example with a dataframe
(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}))
# The result is 4 columns, 2 aggregated columns showing the average of POPESTIMATE2010 & POPESTIMATE2011
# the other 2 aggregated columns showing the sum of POPESTIMATE2010 & POPESTIMATE2011

# %%
# The confusion can come in when we change the labels of the dictionary
# we passed to aggregate, to correspond to the labels in our group data

# In this case pandas recognizes that they're the same and maps the funtions 
# directly to columns instead of creating a hierarchically labelled column (previous example "avg" and "sum") 

# Be aware when using the same name for the columns dataframe and the groupby dictionary names
(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))

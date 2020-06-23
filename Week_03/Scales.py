# %%
import pandas as pd
import numpy as np
# Added due to the third example
from pandas.api.types import CategoricalDtype

# %%
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
df

# %%
# Instruct Pandas to render this as categorical data
df['Grades'].astype('category').head()

# %%
# The commented part below is showed in the course, however to work there is a need to update it via CategorialDtype, as the astype method no longer accepts them
#grades = df['Grades'].astype('category',
                             #categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             #ordered=True)

# Indicate to Pandas that this data is in a logical order
grades = df['Grades'].astype(CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],ordered=True))

grades.head()
# ordinal data has ordering, so it can help you with Boolean Masking

# %%
# Boolean masking
grades > 'C'

# %%
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]

# It's commented below because agg function, shown in the course, needs to be updated
#df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(Avg = np.average)

# Cut = takes in argument which is some real like structure of a column or dataframe or a series
# It also takes a number of bins to be used and all bins are kept at equal spacing
#pd.cut(df['Avg'],10)
df['range'] = pd.cut(df['Avg'],10)
# %%

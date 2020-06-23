# %%
import pandas as pd
import numpy as np
# Added due to the third example
from pandas.api.types import CategoricalDtype

# %%
#http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64
df = pd.read_csv('cars.csv')
df.head()

# %%
# Pivot table is a way of summarizing  data in a data frame for a particular purpose 
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)

# %%
# A pivot table also tends to includes marginal values as well,
# which are the sums for each column and row
# This allow us to see the relationship between 2 variables 
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)

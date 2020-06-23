# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Timestamp
#DatetimeIndex
#Period
#PeriodIndex

# %%
### Timestamp
pd.Timestamp('9/1/2016 10:05AM')

# %%
### Period
pd.Period('1/2016')
pd.Period('3/5/2016')

# %%
### DatetimeIndex
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
t1
type(t1.index)


# %%
### PeriodIndex
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
t2
type(t2.index)

# %%
### Converting to Datetime
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
ts3

# %%
ts3.index = pd.to_datetime(ts3.index)
ts3

# %%
pd.to_datetime('4.7.12', dayfirst=True)

# %%
### Timedeltas
# timedeltas are differences im time
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016')

# %%
pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')

# %%
### Working with Dates in a Dataframe
# Look at nine measurements, taken bi-weekly, every sunday staring on october 2016
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
dates

# %%
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
df

# %%
df.index.weekday_name
# problem with the last pandas version

# %%
# Calculates the difference of a DataFrame element compared with another element in the DataFrame 
# (default is the element in the same column of the previous row).
df.diff()

# %% Resample the date
df.resample('M').mean()

# %%
# Showing just data that belongs to 2017
df['2017']

# %%
# Showing just the data that belongs to 12/2016
df['2016-12']

# %%
# Showing the data that from 12/2016
df['2016-12':]

# %%
df.asfreq('W', method='ffill')


# %%
# Using matplotlib.pyplot package in order to plot a figure
df.plot()

# %%

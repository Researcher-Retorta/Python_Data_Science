import pandas as pd
import numpy as np

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s,"\n")

# querying with iloc (using number)
print(s.iloc[3])
# or
print(s[3]) # Avoid (Not the best way)

# querying with loc (using label)
print(s.loc['Golf'])
# or
print(s['Golf']) # Avoid (Not the best way)

# Example of dictionary and the wrong querying process
sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
print(s)
# s[0] #This won't call s.iloc[0] as one might expect, it generates an error instead

# Example of a series
s = pd.Series([100.00, 120.00, 101.00, 3.00])
print(s)

# Sum the series through a loop
total = 0
for item in s:
    total+=item
print(total)

# Sum the series trhu a standard numpy function
total = np.sum(s)
print(total)

## This creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
s.head()
print(len(s))

# First time performance comparison (EX1 & EX2) 
# EX1
summary = 0
for item in s:
    summary+=item
# 2.01 ms ± 327 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

# EX2
summary = np.sum(s)
# 274 µs ± 259 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


# Second time performance comparison (EX3 & EX4) 
# EX3
s = pd.Series(np.random.randint(0,1000,10000))
for label, value in s.iteritems():
    s.loc[label]= value+2
# 1.48 s ± 23.7 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

#EX4
s = pd.Series(np.random.randint(0,1000,10000))
s+=2 #adds two to each item in s using broadcasting
# 1.13 ms ± 1.99 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

# Pandas Series with number and string
s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
print(s,"\n")

# Bundling different series in one (original_sports + cricket_loving_countries = all_countries)
original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)

print(original_sports,"\n") # original_sports pandas series

print(cricket_loving_countries,"\n") # cricket_loving_countries pandas series

print(all_countries,"\n") # all_countries pandas series (accrue of the two previous series)

## Searching in the all_countries series the label (loc) os a specific sport, in this case Cricket
print(all_countries.loc['Cricket'])

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# Simple distribution, such as flipping a coin (50% heads & 50% tails)
# Run just one time, and the chance to get a zero equals to 0.5
np.random.binomial(1, 0.5)

# %%
# Run 1000 times and the chance to get a zero equals to 0.5
np.random.binomial(1000, 0.5)/1000

# %%
#Chance to have a tornado while filming
chance_of_tornado = 0.01/100
np.random.binomial(100000, chance_of_tornado)

# %%
chance_of_tornado = 0.01

tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
    
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
    if tornado_events[j]==1 and tornado_events[j-1]==1:
        two_days_in_a_row+=1

print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))
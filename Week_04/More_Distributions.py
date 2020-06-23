# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
np.random.uniform(0, 1)

# %%
np.random.normal(0.75)

# %%
distribution = np.random.normal(0.75,size=1000)

# Calculating the standard deviation thru its formula
np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution))

# %%
# Calculating the standard deviation thru a built in function
np.std(distribution)

# %%
# Using scipy built in functions
import scipy.stats as stats
stats.kurtosis(distribution)

# %%
stats.skew(distribution)

# %%
chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)

# %%
chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df5)

# %%
import matplotlib
import matplotlib.pyplot as plt

output = plt.hist([chi_squared_df2,chi_squared_df5], bins=50, histtype='step', 
                  label=['2 degrees of freedom','5 degrees of freedom'])
plt.legend(loc='upper right')
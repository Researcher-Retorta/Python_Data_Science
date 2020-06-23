# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# %%
df = pd.read_csv('grades.csv')
df.head()
len(df)

# %%
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']

# %%
early.mean()

# %%
late.mean()

# %%
from scipy import stats


# %%
# T- testing built in function
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])

# %%
# T- testing built in function
stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])

# %%
# T- testing built in function
stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])
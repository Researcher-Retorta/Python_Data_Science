import numpy as np

# Let's create a new 4 by 3 array of random numbers 0-9.
test = np.random.randint(0, 10, (4,3))
print(test)

# Iterate by row:
for row in test:
    print(row)

# Iterate by index:
for i in range(len(test)):
    print(test[i])

## Iterate by row and index:
for i, row in enumerate(test):
    print('row', i, 'is', row)

# Use zip to iterate over multiple iterables.
test2 = test**2
print(test2)

for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j)

import numpy as np

# Numpy has many built in math functions that can be performed on arrays.
a = np.array([-4, -2, 1, 3, 5])
print(a)
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())

# argmax and argmin return the index of the maximum and minimum values in the array.
print(a.argmax())
print(a.argmin())
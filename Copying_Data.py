import numpy as np

# Let's look at a multidimensional array.
r = np.arange(36)
r.resize((6, 6))
print(r)

# Be careful with copying and modifying arrays in NumPy!
# r2 is a slice of r
r2 = r[:3,:3]
print(r2)

# Set this slice's values to zero ([:] selects the entire array)
r2[:] = 0

## r has also been changed!
print(r)

# To avoid this, use r.copy to create a copy that will not affect the original array
r_copy = r.copy()
print(r_copy)

# Now when r_copy is modified, r will not be changed.
r_copy[:] = 10
print(r_copy, '\n')
print(r)

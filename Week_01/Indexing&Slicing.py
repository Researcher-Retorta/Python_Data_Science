import numpy as np

s = np.arange(13)**2
print(s)

# Use bracket notation to get the value at a specific index. Remember that indexing starts at 0.
print(s[0], s[4], s[-1])

# Use : to indicate a range. array[start:stop]
# Leaving start or stop empty will default to the beginning/end of the array.
print(s[1:5])
print(s[-4:]) # Use negatives to count from the back.

# A second : can be used to indicate step-size. array[start:stop:stepsize]
# Here we are starting 5th element from the end, and counting backwards by 2 until the beginning of the array is reached.
print(s[-5::-2])

# Let's look at a multidimensional array.
r = np.arange(36)
r.resize((6, 6))
print(r)

# Use bracket notation to slice: array[row, column]
print(r[2, 2])

# And use : to select a range of rows or columns~
print(r[3, 3:6])

# Here we are selecting all the rows up to (and not including) row 2, and all the columns up to (and not including) the last column.
print(r[:2, :-1])

# This is a slice of the last row, and only every other element.
print(r[-1, ::2])

# We can also perform conditional indexing. Here we are selecting values from the array that are greater than 30. (Also see np.where)
print(r[r > 30])
# Here we are assigning all values in the array that are greater than 30 to the value of 30.
r[r > 30] = 30
print(r)


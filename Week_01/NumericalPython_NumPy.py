import numpy as np

# Create a list and convert it to a numpy array
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

# Or just pass in a list directly
y = np.array([4, 5, 6])
print(y)

# Pass in a list of lists to create a multidimensional array.
m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)

# Use the shape method to find the dimensions of the array. (rows, columns)
print(m.shape)

# arange returns evenly spaced values within a given interval.
n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
print(n)

# reshape returns an array with the same data with a new shape.
n = n.reshape(3, 5) # reshape array to be 3x5
print(n)

# linspace returns evenly spaced numbers over a specified interval.
o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
print(o)

# resize changes the shape and size of array in-place.
o.resize(3, 3)
print(o)

# ones returns a new array of given shape and type, filled with ones.
print(np.ones((3, 2)))

# zeros returns a new array of given shape and type, filled with zeros.
print(np.zeros((2, 3)))

# eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
print(np.eye(3))

# diag extracts a diagonal or constructs a diagonal array.
print(np.diag(y))

# Create an array using repeating list (or see np.tile)
print(np.array([1, 2, 3] * 3))

# Repeat elements of an array using repeat.
print(np.repeat([1, 2, 3], 3))

# Combining Arrays
p = np.ones([2, 3], int)
print(p)

# Use vstack to stack arrays in sequence vertically (row wise).
print(np.vstack([p, 2*p]))

# Use hstack to stack arrays in sequence horizontally (column wise).
print(np.hstack([p, 2*p]))


import numpy as np

# Use +, -, *, / and ** to perform element wise addition, subtraction, multiplication, division and power.
mylist = [1, 2, 3]
x = np.array(mylist)

y = np.array([4, 5, 6])

print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]

print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]

print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]

print (x.dot(y)) # dot product  1*4 + 2*5 + 3*6 = 32

z = np.array([y, y**2])
print(len(z)) # number of rows of array

# Let's look at transposing arrays. Transposing permutes the dimensions of the array.
z = np.array([y, y**2])
print(z)

# The shape of array z is (2,3) before transposing.
print(z.shape)

# Use .T to get the transpose.
print(z.T)

# The number of rows has swapped with the number of columns.
print(z.T.shape)

# Use .dtype to see the data type of the elements in the array.
print(z.dtype)

# Use .astype to cast to a specific type.
z = z.astype('f')
print(z.dtype)
import sys
import numpy as np

a = np.array([1, 2, 3, 4])
a.dtype # returns data type of array
# casting array to different data type
a = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.int8)
a = np.arange(4) # creates array with evenly spaced elements between 0-4

# create multi-dim arrays:
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
A.shape # returns shape as format (r, c)
A.ndim # number of dimensions
A.size # number of elements
a.dtype # returns data type

# accessing element
A[r][c]
A[r, c] # A[d1, d2, d3, ...]
    # using this format allows for selecting multi
    A[0:2] # selects rows 0-1
    A[:, :2] # selects all rows, first two columns
    a[0, 1:-1:2] # gets first row, elements between 1 and second to lat(exclusive), startindex:endindex:stepsize
# setting an entire row
A[2] = 99 # sets entire third row to 99
a[[0, 3, 4]] # selects specific elements in array
# mixing specific elements and ranges
a[ [0, 4, 5], 3:] # rows 0, 4 and 5, columns 3 and after

# Initializing
np.zeroes((2,3)) # 2x3 full of zeroes
np.ones() # fill w/ one
np.full((2,2), 99) # 2x2 full of 99's
    np.full(a, 4) # uses size of another array(a in this case)
np.random.rand(4,2) # random decimal numbers, pass in shape
np.random.randint(2, 7, size=(3,3)) # returns random ints between 2 and 7(exclusive)
np.identity(3) # returns identity matrix of 3
# repeating array
np.repeat(arr, 3, axis=0) # creating new array by repeating

# summary stats
a.sum() # sum of elements
a.mean() # mean of elements
a.std() # standard deviation
a.var() # variance
# can pass in axis parameter(like dimension)
# for example, the following sums of the rows
a.sum(axis=0)
a.min()
a.max()

a.copy() # makes copy of array; do NOT use = to copy

# Vectorized operations
a + 10 # adds to each element, hote this operation creates new vector and doesn't change original
a + b # can operate between two arrays(these arrays must have same shape)

# Boolean arrays; use bool values to select values in array
a[[True, False, False, True]] # returns array containing first and last element
# use conditions to get bool array
a[ a >= 2] # returns all elements but first two; i.e. [False, False, True, True]
a[ ~(a > a.mean())] # returns all values NOT greater than mean
# and and or operators can also be used
a[(a <= 2) | (a % 2 == 0)]
np.any(filedata > 50, axis=0) # checks if any column has val greater than 50
np.all(filedata > 50, axis=0) # checks if any column has all vals greater than 50

# linear algebra
A.dot(B) # dot product
A @ B # cross product
B.T # transpose
np.matmul(a, b) # cols_b == rows_a
np.linalg.det(c) # finds determinant of matrix

np.reshape()
np.vstack(a, b) # adds each array together as new row
np.hstack(a, b) # adds each array together as new column

#loading from file
filedata = np.genfromtext('data.txt', delimter=',')
filedata.astype('int32')

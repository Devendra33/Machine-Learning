# practising the numpy basics!

import numpy as np

# creating 1D and 2D Arrays

arr = np.array([1,2,3,4,5,6])
arr1 = np.array([[1.3,2.5,3],[4,5,6]], dtype = np.int32)

# Dimention of array
arr.ndim    # 1
arr1.ndim    # 2

arr1.dtype # tells the data type of array
arr1.shape # tells the row x col
arr1.size  # number of elements in the array (6)

# to change the shape of array
arr1.reshape(3,2)  # ROWS * COLS  = Number of elements in the array (MUST CONDITION)

# To convert N-Dimention array to 1D array
arr1 = arr1.ravel()  

# min and max operation
arr1.min()
arr1.max()
arr1.sum(axis = 0)   # axis 0 for column and 1 for row

# for mathematical operation
np.sqrt(arr1)   # return matrix of square rooted elements 
np.std(arr1)   # standard deviation of all element in the matrix

# if we apply +,-,*,/ on numpy array(dimention must be same else error.) then it performs mathematical operations
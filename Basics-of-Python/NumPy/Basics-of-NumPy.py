import numpy as np

# Creating a Single-Dimension array
'''
my_list=[1,2,3,4,5]
array=np.array([1,2,3,4,5])
print(array)
print(my_list*2,array*2) # Difference 1
'''

# Creating Multi-Dimensional arrays
'''
a1=np.array('Hello')
a2=np.array([1,2,3,4])
a3=np.array([[1,2,3,4], # Suppose this as a 3x4 Matrix
             [5,6,7,8],
             [9,10,11,12]])
print(a1,a1.ndim) # 0D
print(a2,a2.ndim) # 1D
print(a3,a3.ndim) # 2D
print(a3.shape)

print(a3[0][2]) # Access 1st row with the '0' index, and 3rd element with '2' index
sum_of_elemets=0
for i in range(0,3):
    for j in range(0,4): sum_of_elemets+=a3[i,j] # Same as a3[i][j]
print(sum_of_elemets)
'''

# Slicing (array[start:stop:jump])
'''
matrix_A=np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])
print(matrix_A[0:2])
print(matrix_A[:,0]) # Select all rows' 0 index element
print(matrix_A[0:2:1,0:2:1]) # Select rows 0 and 1, and select columns 0 and 1
print(matrix_A[:,2::-1])
'''

# Scalar Arithmetic
'''
ar=np.array([1,2,3,4])
print(ar*2)
print(ar+2)
print(ar/2)
print(ar**3)
'''

# Vector Arithmetic
'''
ar2=np.array([1,2,3,4,5])
ar3=np.array([1.2,3.99,8.5,7.5])
print(np.sqrt(ar2))
print(np.round(ar3))
print(np.floor(ar3)) # Similarly can use ceil function
print(np.pi)

# Exercise
radii=np.array([1,2,3])
print(np.pi*radii**2)
'''

# Element-wise Arithmetic
'''
array1=np.array([1,2,3])
array2=np.array([4,5,6])
print(array1+array2)
print(array1*array2)
print((array2**array1).tolist()) # .tolist() convert array to list
'''

# Comparison Operators
'''
scores=np.array([91,55,100,73,82,64])
print((scores>=75).tolist())
scores[scores<60]=0 # If condition satisfied replace those elements with x
print(scores)
'''

# Broadcasting (Operations on diff. shapes by virtually expanding dimensions to that of larger array)
# Broadcasting occurs if no. of col,/rows match or is 1
'''
eg_array1=np.array([[0,0,0],
                   [10,10,10],
                   [20,20,20],
                   [30,30,30]])
eg_array2=np.array([1,2,3]) # This array gets stretched to upper array's size
print(eg_array1+eg_array2)
eg1=np.array([1,2,3,4])
eg2=np.array([[1],[2],[3],[4]])
print(eg1*eg2) # Columns are read first and virtually expanded, then rows for 2D Arrays
'''
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
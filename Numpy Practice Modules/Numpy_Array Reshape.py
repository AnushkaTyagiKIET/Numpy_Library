#In Python Numpy, the Number of Elements in each dimension of an array is called the shape. 
#To reshape the number of dimension of an array is by numpy.reshape() method in Python
#1. Reshape dimensions from 1D to 2D
import numpy as np
n1=np.array([1,23,43,65])
print(n1.reshape(2,2))
#2. Convert 3D to 1D also called flattening
n2=np.array([[[89,994,45,32]],[[988,43,333,45]]])
print(n2.reshape(-1))
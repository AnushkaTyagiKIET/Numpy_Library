#Dimension of the array can also be refered as Rank of them
#with that we will also see how to create 1D, 2D, and 3D arrays
import numpy as np
n1=np.array([1,2,3,4,5]) # 1D array
n2=np.array([[11,2,3,44,54],[22,44,56,65,6]]) # 2D Array
n3=np.array([[[2,3,45,5,7]],[[4,66,33,554,4]]])# 3D Array
print("Dimension of array n1=",n1.ndim)
print("Dimension of array n2=",n2.ndim)
print("Dimension of array n3=",n3.ndim)
#Slicing the array in a range from start to end is what we call Array Slicing.
# It includes the start index but excludes the end Index.
#arr[start:end] here end is excluded
# We also have an parameter named step which tells a jump of elements.
#arr[start:end:step]
import numpy as np
#1. In a 1D Array
n1=np.array([1,23,43,65])
print(n1[0:3])
#2. In a 2D Array
n2=np.array([[34,87,76,56],[38,29,65,98]])
print(n2[0,1:3])
print(n2[1,2:3])
#3. In a 3D Array
n3=np.array([[[89,994,45,32]],[[988,43,333,45]]])
print(n3[0,0,0:3])
print(n3[1,0,1:3])
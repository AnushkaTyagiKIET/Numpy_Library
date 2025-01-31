#Array Indexing in Numpy
#index 0 is element 1
#index 1 is element 2
#index 2 is element 3
#index 3 is element 4 and so on
import numpy as np
n1=np.array([1,2,3,4])
n2=np.array([[2,3,5,6],[2,8,9,1]])
n3=np.array([[[8,7,5,7]],[[88,77,99,6]]])
# 1. Access Elements from 1D array
print("Access Elements from 1D array",n1[3])
# 2. Access Elements from 2D array
print("Access Elements from 2D array",n2[1,3])
# 3. Access Elements from 3D array

print("Access Elements from 3D array",n3[0,0,1])


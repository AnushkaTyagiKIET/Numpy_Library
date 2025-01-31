#It means to break a numpy array into Multiple arrays. Use the array_split method.
# Syntax: array_split(arr_name,split_num)
import numpy as np
n1=np.array([1,23,43,65])
resarr=np.array_split(n1,2)
print("Original",n1)
print("After BEING SPLITTED",resarr)
print("1st Index of splitted arr:",resarr[0]) 
print("2st Index of splitted arr:",resarr[1])
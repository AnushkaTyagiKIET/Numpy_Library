#1. in numpy we can search for a specic value index by using numpy.where() method
import numpy as np
n1=np.array([100,23,43,65])
res=np.where(n1==65)
print("result found at :",res)

#2. Sort-in-Dimensional Numpy Integer Array
print("original array",n1)
print("Sorted array",np.sort(n1))

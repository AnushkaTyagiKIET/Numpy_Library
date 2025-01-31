# perform arithmetic operations on Numpy array using the sum(), substract(), multiply(), divide() methods
import numpy as np

#1. Add Numpy arrays
#        (i) Add all elements of a NumPy arrays.
n1=np.array([100,23,43,65])
n2=np.array([2,4,6,7])
resarr=np.sum([n1,n2])
print("Sum of each elements at once",resarr)
#        (ii)Add column values using the axis parameter. 
resarr1=np.sum([n1,n2], axis=0)
print("sum column wise",resarr1)
#        (iii)Add individual array values using the axis parameter
resarr2=np.sum([n1,n2],axis=1)
print("sum row wise",resarr2)
#2. Substract Numpy arrays
resarr3=np.subtract(n1,n2)
print("substraction result", resarr3)
#3. Multiply Numpy Arrays
resarr4=np.multiply(n1,n2)
print(" Multiply result", resarr4)
#4. Divide Numpy Arrays
resarr5=np.divide(n1,n2)
print(" Divide result", resarr5)
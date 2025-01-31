#One can join two or more arrays in single new array using the following:
# Concatenate() Method:
import numpy as np
n1=np.array([1,23,43,65])
n2=np.array([3,4,5,6])
resarr=np.concatenate((n1,n2))
print("New Array After Joining",resarr)
# By using Stack Method
# such as 1. stack()
         #2. hstack(): stack along rows
         #3. vstack(): stack along columns
         #4. dstack(): stack along depth i.e height
         #5. column_stack():stack as per the columns 
resarr1=np.stack((n1,n2))
print(resarr1)
print("new dimension of array after being stacked=",resarr1.ndim)
resarr2=np.hstack((n1,n2))
print(resarr1)
print("new dimension of array after hstack =",resarr2.ndim)
resarr3=np.vstack((n1,n2))
print(resarr3)
print("new dimension of array after vstack=",resarr3.ndim)
resarr4=np.dstack((n1,n2))
print(resarr4)
print("new dimension of array after dstack=",resarr4.ndim)
resarr5=np.column_stack((n1,n2))
print(resarr5)
print("new dimension of array after column_stack=",resarr5.ndim)
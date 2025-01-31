import numpy as np
n1=np.array([1,2,3,4])
n2=np.array([1,10,4,50])
for i in n1:
    print("Iterating elements of n1",i)
for j in n2:
    print("Itterating elements of n2",j)
resarr=np.setdiff1d(n1,n2)
#in its reverse case
resarr1=np.setdiff1d(n2,n1)
print("Uncommon elements of arrays",resarr)
print("Uncommon elements of arrays",resarr1)
#If you want to get the Intersection of Two arrays, use the intersect1d() method in NumPy. 
#Intersection means finding common Elements between two arrays. 
#In this Lesson, We will see some examples:
#1. Find the Intersection between the 2 arrays
#2. Finding intersection between unsorted arrays sort the resultant array
#3. Find the Intersection between two arrays with different elements
import numpy as np
n1=np.array([1,2,3,4])
n2=np.array([1,10,4,50])
for i in n1:
    print("Iterating elements of n1",i)
for j in n2:
    print("Itterating elements of n2",j)
resarr=np.intersect1d(n1,n2)
print("Intersection of arrays",resarr)
# intersection1d() not only finds intersection elements but also sorts the result. 
n3=np.array([60,8,29,77,1])
n4=np.array([80,50,60,8,1])
resarr1=np.intersect1d(n3,n4)
print(resarr1)
n5=np.array([60,8,29,77,1])
n6=np.array([80,5,6,80,10])
resarr2=np.intersect1d(n5,n6)
print("No elements common",resarr2)
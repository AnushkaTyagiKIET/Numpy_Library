#Specifying axes will calculate values along that specific axes only. we have the min() method and axis attribute
import numpy as np
n=np.array([[100,20,66,70,80],[15,25,35,45,55],[2,5,6,7,9]])
print("\n Minimum Value",n.min())
print("minimum value with axis 0 (vertical)",n.min(axis=0))
print("minimum value with axis 1 (horizontal)",n.min(axis=1))
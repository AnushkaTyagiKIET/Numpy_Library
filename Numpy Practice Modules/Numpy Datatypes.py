#Numpy Datatypes .It supports the following data types:
#b-boolean
#u-Unsigned Integer
#f-float
#c-complex float
#m-time delta
#M-datatime
#O-Object
#S-string
#U-unicode String

import numpy as np
#1. Get the Datatype of a NumPy array with Integers
n=np.array([1,2,3,4])
print("Data Type of Array n",n.dtype)
#2. Get the Datatype of a NumPy array with String
n1=np.array(['2','3','4','5'])
print("Data Type of array n1:",n1.dtype)
#3. Set the Datatype Size within a NumPy array.
n2=np.array(object=['8','9','77'],dtype='S1')
print("Data type of Array n2",n2.dtype)
#4. Convert one Datatype to Another
# for this use astype() to create a copy of an array and then set the new data type.
conv_array=n1.astype('i')
print("Data type of Converted array",conv_array.dtype)
 
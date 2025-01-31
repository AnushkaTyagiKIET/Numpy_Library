#To work with Random Numbers , Numpy has a module called random. To use the moduLe, import it at the beginning as shown below
from numpy import random
# we use the randint() method for this purpose
#1. Generate a random number
# get random number from 0 to 10
n=random.randint(10)
print("Random Number between 0 to 10 = ",n)
#2. Generate a random Array with fixed size
# for this purpose we will be using the parameter of size 
# so if size is 3 it means 3 randomly generated elements will be given in form of array
n1=random.randint(10,size=(3))
print("randomly generated number as per size",n1)
#3. Generate one of the random values based on an array of values
# for this we will use choice method of random module
n2=random.choice([69,23,10,30,90,45,32,12,13,14,15])
print("random variables from given array =",n2)


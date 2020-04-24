#Reshaping the array objects

import numpy

a=numpy.array([[1,3],[4,6],[7,9]])

print(a)
#to find the shapre of arry
print(a.shape)

#After changing the shape of arry

k=a.reshape(2,3)

print(k)
print(k.shape)
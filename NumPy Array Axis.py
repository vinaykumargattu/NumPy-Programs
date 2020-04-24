
#finding maximum element among each column & row

import numpy

a=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(max(a[0]))
print(a.max(axis=0))
print(a.max(axis=1))
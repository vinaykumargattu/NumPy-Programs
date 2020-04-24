#uninitialized array of specified shape and data type

import numpy as np

a=np.empty((3,2))
print(a)

b=np.zeros((2,2))

print(b)

c=np.ones((3,3),dtype=int)

print(c)
print(c.dtype)
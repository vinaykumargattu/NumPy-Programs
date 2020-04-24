import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])

#Arrays vertically concatenated

print(np.vstack((a,b)))

#Arrays horizontally concatenated

print(np.hstack((a,b)))

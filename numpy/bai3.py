import numpy as np
ar= np.zeros((8,8))

for col in range(ar.shape[1]):
    if col % 2 != 0:
        ar[0:-2, col]= 1
    else:
        ar[-1,col]= 1
print(ar)

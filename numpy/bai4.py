import numpy as np
l= [[34,43,73], [82,22,12], [53,94,66]]
ar = np.array(l)
max=ar[0][0]
for row in range(ar.shape[0]):
    for col in range(ar.shape[1]):
        if ar[row][col] > max:
            max = ar[row][col]
        if ar[row][col]== max:
            index=(row,col)
print('số lớn nhất: ',max)
print('vị trí lớn nhất là: ',index)
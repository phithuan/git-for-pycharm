import numpy as np
arr= [
    [14,2,5],
    [3,6,21],
    [55,7,23],
    [32,12,5]
]#đang là kiểu dử liệu list

a=np.array(arr)
print(a.shape)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j]==5:
            print(i,j)

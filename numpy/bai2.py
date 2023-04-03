import numpy as np
row = int(input("nhập số hàng: "))
col = int(input("nhập số cột: "))

arr= np.ones((row, col))
arr[0, :] = 0
arr[col-1, :] = 0
arr[:, 0] = 0
arr[:, row-1] = 0  #or

"""arr[1:-1,1:-1] =0"""
print(arr)


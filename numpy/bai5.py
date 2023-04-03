import numpy as np
l= [[34,43,73], [82,22,12], [53,94,66]]
arr=np.array(l)
print(arr)
print("--------------------")
#swap 2 col
for row in range(arr.shape[1]):
    swapcol= arr[row][::-1]
    print(swapcol)

#đổi chỗ 2 hàng đầu cho nhau

ar_change0= tuple(arr[0,:])#hàng 0 cột lấy tất cả
arr[0]=arr[1]
arr[1]=ar_change0

print(arr)

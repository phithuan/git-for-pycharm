import numpy as np
import pandas as pd
l = [1, 9, 4]#đang là kiểu dử liệu list
a = np.array(l)#chuyển qua nd array

arr= [
    [14,2,5],
    [3,6,2123232],
    [55,7,234],
    [32,12,5]
]#đang là kiểu dử liệu list
a=np.array(arr)#chuyển kiểu dữ liệu qua nd array
#kiểm tra mảng 1 chiều or 2 chiều...(.ndim)
print("số chiều của mảng là: ", a.ndim)

#kiểm tra số hàng và cột (shape)
print("size: hàng và cột là: ", a.shape)

#kiểm tra số phần tử của mảng
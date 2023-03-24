import numpy as np
import pandas as pd
l = [1, 9, 4]#đang là kiểu dử liệu list
a = np.array(l)#chuyển qua nd array

arr= [
    [14,2,5],
    [3,6,21],
    [55,7,23],
    [32,12,5]
]#đang là kiểu dử liệu list
a=np.array(arr)#chuyển kiểu dữ liệu qua nd array
#kiểm tra mảng 1 chiều or 2 chiều...(.ndim)
print("số chiều của mảng là: ", a.ndim)

#kiểm tra số hàng và cột (shape)
print("hàng và cột là: ", a.shape)

#kiểm tra số phần tử của mảng
print("size: ", a.size)

# nếu là đang ở kiểu dữ liệu khác    np.array(l).reshape(row,column)
x=a.reshape(3,4)#reshape lại số hàng và  cột dựa trên số phần tử
print(x)

print("-------------")
print(x[0, :])
print(x[:, 1])
print((x[0:2, 1:3]))

print("----------------------------------------------------------------------------------------------------------------")

z=np.linspace(1,10,5)
print(z)
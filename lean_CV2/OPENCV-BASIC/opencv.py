import random

import cv2
#đọc ảnh
image = cv2.imread("coconut-tree-1892861_960_720.png",1)
image=cv2.resize(image,(0,0),fx=1.3,fy=1.3)#thay đổi theo tỉ lệ
#xoai ảnh
image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE) #XOAY 90 độ thuận chiều block
print(image)              #ROTATE_90_COUNTERCLOCKWISE #Ngược chiều kim đồng hồ
print(type(image))
print(image.shape)#Với phương thức shape() , có thể linh hoạt lấy kích thước của bất kỳ đối tượng Python nào. Có, nó trả về một giá trị bộ cho biết kích thước của một đối tượng Python. Để hiểu đầu ra, bộ dữ liệu được trả về bởi phương thức shape() là số phần tử thực sự đại diện cho giá trị của chiều của đối tượng.

for i in range(100):
    for j in range(image.shape[1]):
        image[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
vungchon=image[0:100,200:400]
image[300:400,150:350]=vungchon
cv2.imshow("anh",image)
n=cv2.waitKey()

if n==ord("s"):#nếu nhắn phím bất kì có n bằng s
    cv2.imwrite("anhmoi.png",image)#thì lưu ảnh
print(n)
cv2.destroyAllWindows()
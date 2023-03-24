import cv2
cap = cv2.VideoCapture("HN.mp4")
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # chiều rộngq
    height = int(cap.get(4))  # chiều cao
#vẽ line
    img=cv2.line(frame,(0,0),(width,height),(0,0,0),5)#(frame,bắt đầu,kết thúc,màu,độ dày)
    img = cv2.line(frame, (0,height), (width,0), (125, 55, 255), 5)
    img = cv2.line(frame, (0,height//2), (width,height//2), (125, 55, 255), 5)
#vẽ hcn(rectangle)
    img=cv2.rectangle(frame,(300,300),(100,100),(23,42,55),5)
#vẽ hình tròn(circle)
    img=cv2.circle(frame,(300,300),70,(44,44,44),6)#(frame,tâm, đường kính,màu)
#chèn text
    font=cv2.FONT_HERSHEY_TRIPLEX
    img=cv2.putText(frame,"do you like me",(200,height-500),font,1,2)

    frame = cv2.resize(frame, (0, 0), fx=0.9, fy=0.9)  # thay đổi theo tỉ lệ

    cv2.imshow("video for cr",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
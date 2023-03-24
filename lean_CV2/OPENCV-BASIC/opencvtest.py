import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # chiều rộngq
    height = int(cap.get(4))  # chiều cao
    frame = cv2.resize(frame, (0, 0), fx=1.5, fy=1.5)  # thay đổi theo tỉ lệ

    cv2.imshow("video for cr",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
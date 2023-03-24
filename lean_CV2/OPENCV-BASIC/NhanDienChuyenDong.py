import cv2
import numpy as np

# Lấy video từ camera laptop
cap = cv2.VideoCapture(0)

# Đọc ảnh đầu tiên
ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# Khởi tạo bộ phát hiện chuyển động
detector = cv2.createBackgroundSubtractorMOG2()

while True:
    # Đọc ảnh tiếp theo
    ret, frame2 = cap.read()
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Tính toán phép trừ giữa hai ảnh và áp dụng bộ phát hiện chuyển động
    diff = detector.apply(frame2_gray)
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    diff = cv2.dilate(diff, None, iterations=2)

    # Hiển thị kết quả
    cv2.imshow('diff', diff)

    # Nếu nhấn phím 'q' thì thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()

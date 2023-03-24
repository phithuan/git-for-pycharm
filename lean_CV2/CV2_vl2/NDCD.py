import cv2

# Đọc video
cap = cv2.VideoCapture(0)

# Khởi tạo bộ phát hiện chuyển động
motion_detector = cv2.createBackgroundSubtractorMOG2()

# Đọc khung hình đầu tiên
success, frame = cap.read()
gray_prev = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while success:
    # Chuyển đổi khung hình sang định dạng grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Tính toán sự khác biệt giữa khung hình hiện tại và khung hình trước đó
    diff = motion_detector.apply(gray)

    # Áp dụng các bước tiền xử lý để loại bỏ nhiễu
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Tìm kiếm các đối tượng được phát hiện trong khung hình
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Vẽ đường bao cho các đối tượng được phát hiện
    for c in contours:
        if cv2.contourArea(c) > 500:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Hiển thị khung hình kết quả
    cv2.imshow('Motion Detection', frame)
    if cv2.waitKey(25)== ord("q"): # độ trễ 1/1000s , nếu bấm q sẽ thoát
        break

    # Lưu khung hình trước đó
    gray_prev = gray.copy()

    # Đọc khung hình tiếp theo
    success, frame = cap.read()

# Giải phóng bộ nhớ và đóng cửa sổ hiển thị video
cap.release()
cv2.destroyAllWindows()
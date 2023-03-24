import cv2

# Thiết lập thông số cho camera
camera_index = 0
width = 640
height = 480

# Khởi tạo camera               0
camera = cv2.VideoCapture(camera_index)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Khởi tạo bộ phát hiện sự chuyển động
detector = cv2.createBackgroundSubtractorMOG2()

# Lặp vô hạn để đọc từng frame từ camera và thực hiện phép trừ ảnh
while True:
    # Đọc frame từ camera
    ret, frame = camera.read()
    if not ret:
        break

    # Thực hiện phép trừ ảnh để phát hiện sự chuyển động
    motion_mask = detector.apply(frame)

    # Hiển thị ảnh và kết quả phát hiện chuyển động
    cv2.imshow('Frame', frame)
    cv2.imshow('Motion Mask', motion_mask)

    # Thoát nếu nhấn phím q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
camera.release()
cv2.destroyAllWindows()

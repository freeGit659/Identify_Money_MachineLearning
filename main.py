import cv2

# Đọc ảnh từ file
image = cv2.imread('./test.jpg')

# Chuyển ảnh sang định dạng HSV để dễ dàng phát hiện màu xanh
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV', hsv)

# Thiết lập phạm vi của màu xanh trong không gian màu HSV
lower_green = (0, 80, 64)
upper_green = (21, 255, 161)

# Tìm kiếm các vùng có màu nằm trong phạm vi đã thiết lập
mask = cv2.inRange(hsv, lower_green, upper_green)
cv2.imshow('mask', mask)

# Áp dụng phép toán đóng và mở để loại bỏ nhiễu và kết nối các vùng có màu xanh gần nhau
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,10))
cv2.imshow('kernel', kernel)
closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closed_mask', closed_mask)
opened_mask = cv2.morphologyEx(closed_mask, cv2.MORPH_OPEN, kernel)
cv2.imshow('opened_mask', opened_mask)

# Tìm kiếm các contour trong ảnh đã xử lý
contours, hierarchy = cv2.findContours(opened_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Duyệt qua các contour tìm được và vẽ hình chữ nhật xung quanh các contour có diện tích lớn hơn một ngưỡng nào đó (ở đây là 500)
for contour in contours:
    area = cv2.contourArea(contour)

    if area > 100:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Hiển thị ảnh kết quả
cv2.imshow('Result', image)
cv2.waitKey(0)
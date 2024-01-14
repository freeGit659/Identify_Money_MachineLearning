import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
from setuptools.command.egg_info import egg_info

# Đọc ảnh từ file
img = cv2.imread('./50k.jpg')
#
# # Chuyển ảnh sang định dạng HSV để dễ dàng phát hiện màu xanh
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
edged = cv2.Canny(bfilter, 30, 200) #Edge detection

cropped_image = img[180:250, 300:600]

# Display cropped image

print(gray.shape)
cv2.imshow("croed", cropped_image)



reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
print(result)
# keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#
# contours = imutils.grab_contours(keypoints)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
# print(contours)
#
# location = None
# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 10, True)
#     if len(approx) == 4:
#         location = approx
#         break
#
# mask = np.zeros(gray.shape, np.uint8)
# new_image = cv2.drawContours(mask, [location], 0, 255, -1)
# new_image = cv2.bitwise_and(img, img, mask=mask)
#
# (x,y) = np.where(mask==255)
# (x1, y1) = (np.min(x), np.min(y))
# (x2, y2) = (np.max(x), np.max(y))
# cropped_image = gray[x1:x2+1, y1:y2+1]
#
# cv2.imshow('anh xam',edged)
# plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
#
# bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
# edged = cv2.Canny(bfilter, 30, 200) #Edge detection
# plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
#
# keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(keypoints)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
#
# location = None
# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 10, True)
#     if len(approx) == 4:
#         location = approx
#         break
#
# mask = np.zeros(gray.shape, np.uint8)
# new_image = cv2.drawContours(mask, [location], 0,255, -1)
# new_image = cv2.bitwise_and(img, img, mask=mask)
#
# mask = np.zeros(gray.shape, np.uint8)
# new_image = cv2.drawContours(mask, [location], 0,255, -1)
# new_image = cv2.bitwise_and(img, img, mask=mask)
#
# (x,y) = np.where(mask==255)
# (x1, y1) = (np.min(x), np.min(y))
# (x2, y2) = (np.max(x), np.max(y))
# cropped_image = gray[x1:x2+1, y1:y2+1]
#
# plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
# # Thiết lập phạm vi của màu xanh trong không gian màu HSV
# lower_green = (0, 80, 64)
# upper_green = (21, 255, 161)
#
# # Tìm kiếm các vùng có màu nằm trong phạm vi đã thiết lập
# mask = cv2.inRange(hsv, lower_green, upper_green)
# cv2.imshow('Khu mau lay ney', mask)
#
# # Áp dụng phép toán đóng và mở để loại bỏ nhiễu và kết nối các vùng có màu xanh gần nhau
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,10))
# #cv2.imshow('kernel', kernel)
# closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# cv2.imshow('Xac dinh khang mau', closed_mask)
# opened_mask = cv2.morphologyEx(closed_mask, cv2.MORPH_OPEN, kernel)
# #cv2.imshow('Làm rõ các ô màu', opened_mask)
#
# # Tìm kiếm các contour trong ảnh đã xử lý
# contours, hierarchy = cv2.findContours(opened_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Duyệt qua các contour tìm được và vẽ hình chữ nhật xung quanh các contour có diện tích lớn hơn một ngưỡng nào đó (ở đây là 500)
# for contour in contours:
#     area = cv2.contourArea(contour)
#
#     if area > 100:
#         x, y, w, h = cv2.boundingRect(contour)
#         cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
# # Hiển thị ảnh kết quả
# cv2.imshow('Nhan dien ky tu', image)
cv2.waitKey(0)
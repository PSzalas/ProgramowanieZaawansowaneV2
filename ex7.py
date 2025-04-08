import cv2

image = cv2.imread("../ExampleImages/car.jpg")
cv2.imshow("Original", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)

s_up = s+30
s_down = s-30

image_modified_s_up = cv2.merge([h, s_up, v])
image_modified_rgb_s_up = cv2.cvtColor(image_modified_s_up, cv2.COLOR_HSV2BGR)

image_modified_s_down = cv2.merge([h, s_down, v])
image_modified_rgb_s_down = cv2.cvtColor(image_modified_s_down, cv2.COLOR_HSV2BGR)

cv2.imshow("Modified_SUP", image_modified_rgb_s_up)
cv2.imshow("Modified_SDOWN", image_modified_rgb_s_down)

cv2.waitKey(0)
import cv2

image = cv2.imread("../ExampleImages/car.jpg")
cv2.imshow("Original", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)

h = h+30

image_modified = cv2.merge([h, s, v])
image_modified_rgb = cv2.cvtColor(image_modified, cv2.COLOR_HSV2BGR)

cv2.imshow("Modified", image_modified_rgb)

cv2.waitKey(0)
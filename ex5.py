import cv2
import numpy as np

image = cv2.imread("../ExampleImages/pole.jpg")
cv2.imshow("Original", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)

lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Result", res)

cv2.waitKey(0)
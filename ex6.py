import cv2
import numpy as np

image = cv2.imread("../ExampleImages/face.jpg")
cv2.imshow("Original", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)

lower_skin = np.array([0, 20, 70])
upper_skin = np.array([20, 255, 255])

mask = cv2.inRange(hsv, lower_skin, upper_skin)
res = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Result", res)

cv2.waitKey(0)
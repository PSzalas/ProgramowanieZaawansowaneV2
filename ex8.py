import cv2
import numpy as np

image = cv2.imread("../ExampleImages/car.jpg")
cv2.imshow("Original", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h, s, v) = cv2.split(hsv)

lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 30, 255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)

lower_red1 = np.array([0, 100, 50])
upper_red1 = np.array([10, 255, 255])
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([170, 100, 50])
upper_red2 = np.array([180, 255, 255])
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask_red = cv2.bitwise_or(mask_red1, mask_red2)

combined_mask = cv2.bitwise_or(mask_blue, mask_white)
combined_mask = cv2.bitwise_or(combined_mask, mask_red)

result = cv2.bitwise_and(image, image, mask=combined_mask)

cv2.imshow("Mask", combined_mask)
cv2.imshow("Result", result)
cv2.waitKey(0)


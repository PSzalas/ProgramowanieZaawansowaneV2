import numpy as np
import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate(image, 1)
difference = cv2.bitwise_xor(image, rotated)
cv2.imshow("Difference", difference)
cv2.waitKey(0)
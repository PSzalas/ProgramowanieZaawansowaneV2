import cv2
import numpy as np

image = cv2.imread("../ExampleImages/example1.jpg")

numpy_subtract = np.uint8(image) - np.uint8(80)
cv2.imshow("Original", image)
cv2.imshow("Numpy_subtract", numpy_subtract)
cv2_subtract = cv2.subtract(image, 80)
cv2.imshow("Cv2_subtract", cv2_subtract)
cv2.waitKey(0)
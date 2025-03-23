import cv2
import numpy as np

image = cv2.imread("../ExampleImages/example1.jpg")

numpy_added = np.uint8(image) + np.uint8(150)
cv2.imshow("Original", image)
cv2.imshow("Numpy_added", numpy_added)
cv2_added = cv2.add(image, 150)
cv2.imshow("Cv2_added", cv2_added)
cv2.waitKey(0)
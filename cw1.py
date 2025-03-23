import cv2
import numpy as np

image = cv2.imread("../ExampleImages/example1.jpg")

cv2_brightened = cv2.convertScaleAbs(image, alpha=1, beta=50)
M = np.ones(image.shape, dtype="uint8") * 100
numpy_brightened = cv2.add(image, M)
cv2.imshow("Original", image)
cv2.imshow("Numpy_brightened", numpy_brightened)
cv2.imshow("Cv2_brightened", cv2_brightened)
cv2.waitKey(0)

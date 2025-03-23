import cv2
import numpy as np

image = cv2.imread("../ExampleImages/example1.jpg")

cv2.imshow("Original", image)

image[:, :, 2] = np.clip(image[:, :, 2] + 30, 0, 255)
image[:, :, 1] = np.clip(image[:, :, 1] + 20, 0, 255)
image[:, :, 0] = np.clip(image[:, :, 0] + 10, 0, 255)

cv2.imshow("Filtered", image)
cv2.waitKey(0)
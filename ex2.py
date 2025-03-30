import cv2
import numpy as np

image = cv2.imread("../ExampleImages/face.jpg")
cv2.imshow("Original", image)

mask = np.ones(image.shape[:2], dtype="uint8")
cv2.circle(mask, (270, 170), 20, 0, -1)
cv2.circle(mask, (345, 170), 20, 0, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
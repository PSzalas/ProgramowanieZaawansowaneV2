import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 30 Degrees relative to point (0, 0)", rotated)

cv2.waitKey(0)
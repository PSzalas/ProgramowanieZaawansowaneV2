import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate(image, 60)
cv2.imshow("Rotated using imutils", rotated)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
warpAffineRotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated using warpAffine", warpAffineRotated)

cv2.waitKey(0)
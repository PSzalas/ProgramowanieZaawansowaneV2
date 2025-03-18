import cv2
import imutils

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]

resized = imutils.resize(image, width=w//2, height=h//2)
cv2.imshow("Resized", resized)
cv2.waitKey(0)

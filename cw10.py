import cv2
import imutils

image = cv2.imread("../ExampleImages/example1.jpg")
(h, w) = image.shape[:2]

resized = imutils.resize(image, width=500)
cv2.imwrite("../ExampleImages/Example1Resized.jpg", resized)

cv2.waitKey(0)
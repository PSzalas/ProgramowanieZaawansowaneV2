import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate(image, 60)
cv2.imshow("Rotated by 180 degrees using imutils rotate", rotated)

cv2.waitKey(0)
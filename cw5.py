import cv2
import imutils

image = cv2.imread("../ExampleImages/example1.jpg")
image2 = imutils.rotate(image, 1)
difference = cv2.absdiff(image, image2)
cv2.imshow("Difference", difference)
cv2.waitKey(0)
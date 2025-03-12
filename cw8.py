import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)

rotated = image
for i in range(3):
    rotated = imutils.rotate(rotated, 30)
cv2.imshow("Rotated 3 times by 30 degrees", rotated)

rotatedOnce = imutils.rotate(image, 90)
cv2.imshow("Rotated once by 90 degrees", rotatedOnce)

cv2.waitKey(0)
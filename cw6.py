import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated by -33 degrees using imutils rotate_bound", rotated)

cv2.waitKey(0)
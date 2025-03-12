import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
rotated = imutils.rotate(image, 75)
cv2.imwrite("../ExampleImages/rotated_output.jpg", rotated)
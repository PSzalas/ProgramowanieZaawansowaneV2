import imutils
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")

for i in range(0, 361, 15):
    rotated = imutils.rotate(image, i)
    cv2.imshow("Rotation animation", rotated)
    cv2.waitKey(500)

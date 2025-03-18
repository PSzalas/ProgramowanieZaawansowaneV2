import cv2
import imutils

image = cv2.imread("../ExampleImages/example1.jpg")
(h, w) = image.shape[:2]

for scale in range(100, 310, 20):
    width = int(w * (scale/100))
    height = int(h * (scale / 100))
    resized = imutils.resize(image, height=height, width=width)

    cv2.imshow("Resized", resized)
    cv2.waitKey(500)

cv2.waitKey(0)
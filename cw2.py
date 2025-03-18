import cv2

image = cv2.imread("../ExampleImages/example1.jpg")

flipped = cv2.flip(image, 0)
cv2.imshow("Odwrocone w pionie", flipped)
cv2.waitKey(0)
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")

flipped = cv2.flip(image, -1)
cv2.imshow("Odwrocone w pionie i w poziomie", flipped)
cv2.waitKey(0)
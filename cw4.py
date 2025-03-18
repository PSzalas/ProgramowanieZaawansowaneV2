import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Oryginalne", image)

flipped_vertically = cv2.flip(image, 1)
cv2.imshow("Odwrocone w poziomie", flipped_vertically)

flipped_horizontally = cv2.flip(image, 0)
cv2.imshow("Odwrocone w pionie", flipped_horizontally)

flipped = cv2.flip(image, -1)
cv2.imshow("Odwrocone w pionie i w poziomie", flipped)
cv2.waitKey(0)
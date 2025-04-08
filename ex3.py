import cv2

image = cv2.imread("../ExampleImages/grey.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T, threshlnv) = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshlnv", threshlnv)

eroded = cv2.erode(threshlnv, None, iterations=3)

cv2.waitKey(0)
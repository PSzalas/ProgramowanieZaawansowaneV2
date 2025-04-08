import cv2

image = cv2.imread("../ExampleImages/grey.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

(T, threshlnv) = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshlnv30", threshlnv)

(T, threshlnv) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshlnv100", threshlnv)

(T, threshlnv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshlnv200", threshlnv)

cv2.waitKey(0)
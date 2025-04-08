import cv2

image = cv2.imread("../ExampleImages/grey.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
brightened = cv2.add(gray, 50)

(T, threshlnv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshlnvOriginal", threshlnv)

(T, threshlnv) = cv2.threshold(brightened, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshlnvBrightened", threshlnv)

cv2.waitKey(0)
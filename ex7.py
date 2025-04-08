import cv2

image = cv2.imread("../ExampleImages/grey.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T, threshlnv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("ThreshlnvOtsu", threshlnv)

masked = cv2.bitwise_and(image, image, mask=threshlnv)
cv2.imshow("Masked", masked)

cv2.waitKey(0)
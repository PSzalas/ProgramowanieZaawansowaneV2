import cv2
import imutils

image = cv2.imread("../ExampleImages/grey.jpg")
resized = imutils.resize(image, width=300)
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)

(T, threshlnv) = cv2.threshold(resized, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshlnv100", threshlnv)

(T, threshlnv) = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshlnv140", threshlnv)

(T, threshlnv) = cv2.threshold(resized, 180, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshlnv180", threshlnv)

cv2.waitKey(0)
cv2.destroyAllWindows()
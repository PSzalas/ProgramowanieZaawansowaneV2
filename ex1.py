import cv2

image = cv2.imread("../ExampleImages/paving_stone_shadow.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)
cv2.imshow("Adaptive Mean", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 10)
cv2.imshow("Adaptive Gaussian", thresh)

(T, threshlnv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("SimpleThresh", threshlnv)

(T, threshlnv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu", threshlnv)
cv2.waitKey(0)
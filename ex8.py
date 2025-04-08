import cv2

image = cv2.imread("../ExampleImages/grey.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

(T, threshlnv) = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshInv30", threshlnv)
(T, threshlnv) = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshInvBlurred30", threshlnv)
Inv30_eroded = cv2.erode(threshlnv, kernel, iterations=1)
cv2.imshow("Inv30_eroded", Inv30_eroded)

(T, threshlnv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshInv100", threshlnv)
(T, threshlnv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshInvBlurred100", threshlnv)
Inv100_eroded = cv2.erode(threshlnv, kernel, iterations=1)
cv2.imshow("Inv100_eroded", Inv100_eroded)

(T, threshlnv) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshInv200", threshlnv)
(T, threshlnv) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("ThreshInvBlurred200", threshlnv)
Inv200_eroded = cv2.erode(threshlnv, kernel, iterations=1)
cv2.imshow("Inv200_eroded", Inv200_eroded)

(T, threshlnv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("ThreshlnvOtsu", threshlnv)
(T, threshlnv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("ThreshlnvBlurredOtsu", threshlnv)
otsu_eroded = cv2.erode(threshlnv, kernel, iterations=1)
cv2.imshow("OtsuEroded", otsu_eroded)

cv2.waitKey(0)
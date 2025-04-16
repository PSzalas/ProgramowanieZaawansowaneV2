import cv2

image = cv2.imread("../ExampleImages/foreground.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

mask = cv2.adaptiveThreshold(
    blurred,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    41, 10
)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Mask", mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
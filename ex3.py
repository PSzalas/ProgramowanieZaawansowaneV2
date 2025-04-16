import cv2

image = cv2.imread("../ExampleImages/paving_stone_shadow.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

for i in [2, 5, 10, 15]:
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 41, i)
    cv2.imshow(f"Gaussian {i}", thresh)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 41, i)
    cv2.imshow(f"Mean {i}", thresh)

cv2.waitKey(0)
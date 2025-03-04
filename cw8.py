import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]

cv2.imshow('Original', image)

image[100, 0:w] = (0, 255, 0)

cv2.imshow('Green row', image)
cv2.waitKey(0)
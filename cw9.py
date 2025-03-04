import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]

cv2.imshow('Original', image)

image[50:100, 50:100] = (255, 255, 255)

cv2.imshow('White', image)
cv2.waitKey(0)
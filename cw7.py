import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]
(f3X, f3Y) = (w // 3, h // 3)

center_fragment = image[f3Y:f3Y*2, f3X:f3X*2]

cv2.imshow('Original', image)
cv2.imshow('Center Fragment', center_fragment)
cv2.waitKey(0)
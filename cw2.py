import cv2

image = cv2.imread('../ExampleImages/example1.jpg')

(h, w) = image.shape[:2]

cv2.imshow('Original', image)

image[h-1, w-1] = (0,0,255)

cv2.imshow('BGR', image)

cv2.waitKey(0)
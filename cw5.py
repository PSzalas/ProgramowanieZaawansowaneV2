import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

image[0:cY, 0:cX] = (255,0,0)

cv2.imshow('Image', image)
cv2.waitKey(0)
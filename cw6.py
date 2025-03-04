import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

image[cY-50:cY+50, cX-50:cX+50] = (0,0,255)

cv2.imshow('Image', image)
cv2.waitKey(0)
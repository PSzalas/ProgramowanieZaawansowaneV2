import cv2

image = cv2.imread('../ExampleImages/face.jpg')
roi = image[20:300, 220:410]
cv2.imshow("image", image)
cv2.imshow("roi", roi)
cv2.waitKey(0)
import numpy as np
import cv2

image = cv2.imread('../ExampleImages/face.jpg')
image = cv2.resize(image,(640,480))

canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

image = cv2.imread('../ExampleImages/face.jpg')
image = cv2.resize(image,(640,480))
cv2.circle(image, (262,200),10,red,20)
cv2.circle(image, (350,200),10,red,20)
cv2.circle(image, (310,200),150,blue,2)
cv2.rectangle(image,(280,295),(330,285),green,20)

cv2.imshow("Image", image)
cv2.waitKey(0)
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")

roi = image[0:100,0:100]
cv2.imshow("image", image)
cv2.imshow("roi", roi)
cv2.waitKey(0)
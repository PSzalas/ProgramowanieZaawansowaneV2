import cv2

image = cv2.imread("../ExampleImages/example1.jpg")

roi = image[100:200, 100:200]
image[0:100, 0:100] = roi
cv2.imshow("image", image)
cv2.imshow("roi", roi)
cv2.waitKey(0)
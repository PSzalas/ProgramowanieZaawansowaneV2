import cv2

image = cv2.imread("../ExampleImages/example1.jpg")

roi = image[0:300, 0:300]
cv2.imwrite("../ExampleImages/cropped_image.jpg", roi)
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")

(h, w) = image.shape[:2]
roi = image[h//2:h]
cv2.imshow("image", image)
cv2.imshow("roi", roi)
cv2.waitKey(0)
import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]

resized = cv2.resize(image, (w*2,h*2), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
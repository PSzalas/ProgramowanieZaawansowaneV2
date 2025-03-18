import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]

INTER_CUBIC = cv2.resize(image, (w*5,h*5), interpolation=cv2.INTER_CUBIC)
cv2.imshow("INTER_CUBIC", INTER_CUBIC)
INTER_LANCZOS4 = cv2.resize(image, (w*5,h*5), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("INTER_LANCZOS4", INTER_LANCZOS4)
cv2.waitKey(0)
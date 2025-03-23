import cv2

image = cv2.imread("../ExampleImages/example1.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cY, cX) = (h // 2, w // 2)

cutted_image = image[0:h, cX:w]
image[0:h, cX:w] = cv2.flip(cutted_image, 0)
cv2.imshow("Flipped", image)
cv2.waitKey(0)
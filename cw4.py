import cv2

image_gray = cv2.imread('../ExampleImages/example1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('../ExampleImages/example1_grayscale.jpg', image_gray)
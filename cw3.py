import cv2

image_gray = cv2.imread('../ExampleImages/example1.jpg', cv2.IMREAD_GRAYSCALE)
(h, w) = image_gray.shape

print(f'Liczba kanałów: 1')
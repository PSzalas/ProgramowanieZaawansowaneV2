import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w, c) = image.shape

print(f'Liczba kanałów: {c}')
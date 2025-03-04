import cv2

image = cv2.imread('../ExampleImages/example1.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

(b, g, r) = image[cX, cY]
print(f"Pixel at ({cX},{cY}) - Red: {r}, Green: {g}, Blue: {b}")
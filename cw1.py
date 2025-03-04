import cv2

image = cv2.imread('../ExampleImages/example1.jpg')

(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(b, g, r))
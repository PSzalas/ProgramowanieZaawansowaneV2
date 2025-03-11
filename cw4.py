import numpy as np
import cv2
import imutils

image = cv2.imread('../ExampleImages/example1.jpg')

M = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

cv2.imshow("Original", image)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted", shifted)
imutilsShifted = imutils.translate(image, 100, 50)
cv2.imshow("ImutilsShifted", imutilsShifted)
cv2.waitKey(0)
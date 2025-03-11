import numpy as np
import cv2

M = np.float32([
    [1, 0,-20],
    [0, 1, -50]
])

image = cv2.imread('../ExampleImages/example1.jpg')
cv2.imshow("Original", image)

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
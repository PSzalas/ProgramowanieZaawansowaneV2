import cv2
import numpy as np

image = cv2.imread("../ExampleImages/opencv.png")
cv2.imshow("Original", image)

b, g, r = cv2.split(image)
image = cv2.merge([r, g, b])

cv2.imshow("Merged", image)

image = cv2.merge([b, g, np.zeros_like(r)])

cv2.imshow("Merged_Zero", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
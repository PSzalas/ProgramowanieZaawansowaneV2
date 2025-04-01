import cv2
import numpy as np

image = cv2.imread("../ExampleImages/opencv.png")
cv2.imshow("Original", image)

b, g, r = cv2.split(image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (250, 170), 40, 255, -1)
mask_bool = mask.astype(bool)

r[mask_bool] = np.clip(r[mask_bool] - 50, 0, 255)

masked = cv2.merge([b, g, r])
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
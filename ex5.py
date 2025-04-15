import cv2
import numpy as np

example = cv2.imread("../ExampleImages/example1.jpg")
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
img_float = example.astype(np.float32)
noise = np.zeros_like(img_float)
cv2.randn(noise, (0, 0, 0), (30, 30, 30))

noisy_img = cv2.add(img_float, noise)
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)


kernelSizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

cv2.imshow("Original", noisy_img)

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(noisy_img, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)

for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(noisy_img, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)

for k in(3, 9, 15):
    blurred = cv2.medianBlur(noisy_img, k)
    cv2.imshow("Median {}".format(k), blurred)

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(noisy_img, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(
        diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)

cv2.waitKey(0)
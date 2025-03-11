import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

for r in range(0, 181, 20):
    cv2.rectangle(canvas, (150-r, 150-r), (150+r, 150+r), white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
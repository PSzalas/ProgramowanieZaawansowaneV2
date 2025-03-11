import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)

cv2.rectangle(canvas, (100, 100), (200, 200), blue)
cv2.circle(canvas, (150, 150), 30, red)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
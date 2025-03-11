import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0, 255, 0)
red = (0, 0, 255)

cv2.rectangle(canvas, (0, 0), (100, 50), green)
cv2.rectangle(canvas, (197, 247), (297, 297), red, 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
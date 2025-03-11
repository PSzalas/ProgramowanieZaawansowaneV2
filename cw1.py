import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
blue = (255, 0, 0)

cv2.line(canvas, (150, 150), (300, 150), blue, 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
import numpy as np
import cv2

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

triangle_shape = np.zeros((300, 300), dtype="uint8")
pts = np.array([[150, 0], [0, 300], [300, 300]], np.int32)
pts = pts.reshape((-1, 1, 2))
triangle = cv2.fillPoly(triangle_shape, [pts], 255)
cv2.imshow("Triangle", triangle)

bitwise_and = cv2.bitwise_and(triangle, circle)
cv2.imshow("Bitwise_and", bitwise_and)
bitwise_or = cv2.bitwise_or(triangle, circle)
cv2.imshow("Bitwise_or", bitwise_or)
bitwise_xor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("Bitwise_xor", bitwise_xor)
bitwise_not = cv2.bitwise_not(triangle, circle)
cv2.imshow("Bitwise_not", bitwise_not)

cv2.waitKey(0)
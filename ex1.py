import cv2
import numpy as np

image = cv2.imread("../ExampleImages/opencv.png")
cv2.imshow("Original", image)

b, g, r = cv2.split(image)

blue_image = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])
cv2.imshow("Blue channel", blue_image)
cv2.imwrite("../ExampleImages/opencvB.jpg", blue_image)

green_image = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])
cv2.imshow("Green channel", green_image)
cv2.imwrite("../ExampleImages/opencvG.jpg", green_image)

red_image = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])
cv2.imshow("Red channel", red_image)
cv2.imwrite("../ExampleImages/opencvR.jpg", red_image)

cv2.waitKey(0)
cv2.destroyAllWindows()